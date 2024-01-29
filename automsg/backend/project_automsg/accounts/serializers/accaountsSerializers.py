from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name','username')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password],
                                     style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'password2',)
        extra_kwargs = {
            'first_name': {'required': True},
            'username': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance

from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from accounts.permisions import IsSuperuserOrReadOnly
from accounts.serializers.accaountsSerializers import (
    RegisterSerializer,
    ChangePasswordSerializer,
    UpdateUserSerializer,
    UserSerializer,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.conf import settings

User = get_user_model()


# Custom ObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get("access")
            refresh_token = response.data.get("refresh")

            response.set_cookie(
                settings.ACCESS_COOKIE_NAME,
                access_token,
                httponly=True,
                max_age=settings.ACCESS_COOKIE_MAX_AGE,
                secure=settings.AUTH_COOKIE_SECURE,
                path="/",
                samesite="Lax",
            )

            response.set_cookie(
                settings.REFRESH_COOKIE_NAME,
                refresh_token,
                httponly=True,
                max_age=settings.REFRESH_COOKIE_MAX_AGE,
                secure=settings.AUTH_COOKIE_SECURE,
                path="/",
                samesite="Lax",
            )
        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get(settings.REFRESH_COOKIE_NAME)

        if refresh_token:
            request.data["refresh"] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get("access")
            refresh_token = response.data.get("refresh")

            response.set_cookie(
                settings.ACCESS_COOKIE_NAME,
                access_token,
                httponly=True,
                max_age=settings.ACCESS_COOKIE_MAX_AGE,
                secure=settings.AUTH_COOKIE_SECURE,
                path="/",
                samesite="Lax",
            )
            # refresh token must be reset if the blacklist option is enabled in the settings file.
        return response


# for verification purposes if required
class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get(settings.AUTH_COOKIE_NAME)

        if access_token:
            request.data["token"] = access_token

        return super().post(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["first_name", "last_name"]
    permission_classes = (
        IsAuthenticated,
        IsSuperuserOrReadOnly,
    )


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# logout endpoint


@api_view(["POST"])
def logout_view(request):
    try:
        refresh_token = request.COOKIES.get("refresh")
        print(refresh_token)
        token = RefreshToken(refresh_token)
        token.blacklist()

        response=Response(status=status.HTTP_205_RESET_CONTENT)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))



class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

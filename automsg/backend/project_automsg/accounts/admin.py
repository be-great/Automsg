from django.contrib import admin

from accounts.models import AutoMsgUser


# Register your models here.
@admin.register(AutoMsgUser)
class AutoMsgAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'is_staff', 'is_active',  'date_joined', 'last_login')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions',
         {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import RegisterView, LogoutView, ChangePasswordView, UpdateProfileView, UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("change-password/<int:pk>", ChangePasswordView.as_view(), name="change-password"),
    path("update-profile/<int:pk>", UpdateProfileView.as_view(), name="update-profile"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls

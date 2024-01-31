from django.urls import path
from rest_framework.routers import DefaultRouter


from accounts.views import RegisterView, LogoutView, ChangePasswordView, UpdateProfileView, UserViewSet,CustomTokenObtainPairView,CustomTokenRefreshView

router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("change-password/<int:pk>", ChangePasswordView.as_view(), name="change-password"),
    path("update-profile/<int:pk>", UpdateProfileView.as_view(), name="update-profile"),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls

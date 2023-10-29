from django.urls import include, path
from .views import (
    CustomUserViewSet,
    UserViewSet,
    UserLoginViewSet,
    UserRegisterationViewSet,
    UserLogoutViewSet,
)
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"custom-users", CustomUserViewSet, basename="list")
router.register(r"register", UserRegisterationViewSet, basename="register")
router.register(r"login", UserLoginViewSet, basename="login")
router.register(r"logout", UserLogoutViewSet, basename="logout")
router.register(r"user", UserViewSet, basename="user")

urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    # path("", CustomListView.as_view(), name="customuser-list"),
    # path("register/", UserRegistrationView.as_view(), name="signup"),
    # path("login/", UserLoginView.as_view(), name="login"),
    # path("logout/", UserLogoutView.as_view(), name="logout"),
    # path("profile/", UserProfileView.as_view(), name="profile"),
    # path("register/api", UserRegisterationAPIView.as_view(), name="signup-api"),
    # path("login/api", UserLoginAPIView.as_view(), name="login-api"),
    # path("logout/api", UserLogoutAPIView.as_view(), name="logout-api"),
    # path("profile/api", UserAPIView.as_view(), name="profile-api"),
    # path("profile/edit", UserProfileUpdateView.as_view(), name="edit-profile"),
    # path("password/change", PasswordChangingView.as_view(), name="password-change"),
]

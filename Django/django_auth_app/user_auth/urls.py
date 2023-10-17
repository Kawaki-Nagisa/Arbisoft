from django.urls import path
from . import views

app_name = "user_auth"
urlpatterns = [
    path("", views.CustomLoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "<int:id>/password/",
        views.CustomPasswordChangeView.as_view(),
        name="change_password",
    ),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/edit/", views.EditProfileView.as_view(), name="edit_profile"),
]

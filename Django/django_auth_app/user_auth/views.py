from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import LoginForm, SignUpForm, ChangePasswordForm, ProfileForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "user_auth/templates/login.html"


class SignUpView(generic.CreateView):
    template_name = "user_auth/templates/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("user_auth:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Sign Up"
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("user_auth:profile")
        return super().dispatch(request, *args, **kwargs)


class CustomPasswordChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = "user_auth/templates/change-password.html"
    success_url = reverse_lazy("user_auth:profile")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@method_decorator(login_required, name="dispatch")
class ProfileView(generic.UpdateView):
    form_class = ProfileForm
    template_name = "user_auth/templates/main.html"
    success_url = "user:auth:profile"

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "User Profile"
        return context


@method_decorator(login_required, name="dispatch")
class EditProfileView(generic.UpdateView):
    form_class = ProfileForm
    template_name = "user_auth/templates/edit-user.html"
    success_url = reverse_lazy("user_auth:profile")

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Edit Profile"
        return context

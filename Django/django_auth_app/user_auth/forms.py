from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
    AuthenticationForm,
)
from .models import CustomUser

class LoginForm(AuthenticationForm):
    """
    Form for user authentication.
    
    This form allows users to log in using their email and password.

    Attributes:
        Meta (class): Metadata about the form.
            model (CustomUser): The user model to use for authentication.
            fields (tuple): Fields to display in the form.
    """

    class Meta:
        model = CustomUser
        fields = ("email", "password")

class SignUpForm(UserCreationForm):
    """
    Form for user registration.
    
    This form allows users to sign up by providing their email, date of birth,
    blood group, and desired password.

    Attributes:
        date_of_birth (DateField): Field to input the user's date of birth.
        Meta (class): Metadata about the form.
            model (CustomUser): The user model to use for registration.
            fields (tuple): Fields to display in the form.
    """

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "date_of_birth",
            "blood_group",
            "password1",
            "password2",
        )

class ChangePasswordForm(PasswordChangeForm):
    """
    Form for changing user's password.
    
    This form allows users to change their password.

    Attributes:
        Meta (class): Metadata about the form.
            model (CustomUser): The user model to change the password for.
            fields (tuple): Fields to display in the form.
    """

    class Meta:
        model = CustomUser
        fields = ("password",)

class ProfileForm(UserChangeForm):
    """
    Form for updating user's profile information.
    
    This form allows users to update their profile information including
    first name, last name, email, password, date of birth, blood group,
    date joined, and activation status.

    Attributes:
        date_of_birth (DateField): Field to input the user's date of birth.
        Meta (class): Metadata about the form.
            model (CustomUser): The user model to update profile information for.
            fields (tuple): Fields to display in the form.
    """

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "date_of_birth",
            "blood_group",
            "date_joined",
            "is_active",
            "is_superuser",
        )

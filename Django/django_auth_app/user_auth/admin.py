"""
Admin configuration for CustomUser model in the application.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import ProfileForm, SignUpForm


class CustomUserAdmin(UserAdmin):
    """
    Admin class for managing CustomUser instances.

    This class provides a customized admin interface for managing CustomUser instances,
    allowing administrators to view and modify user details in the Django admin panel.

    Attributes:
        add_form: A reference to the sign-up form for adding new users.
        form: A reference to the profile form for modifying user profiles.
        model: A reference to the CustomUser model.
        list_display: Fields to display in the admin list view.
        list_filter: Fields to use for filtering in the admin panel.
        fieldsets: Fieldset configurations for the admin detail view.
        add_fieldsets: Fieldset configurations for the admin add view.
        search_fields: Fields to use for searching users.
        ordering: Fields to determine the default ordering of users.
    """

    add_form = SignUpForm
    form = ProfileForm
    model = CustomUser
    list_display = (
        "email",
        "date_joined",
        "blood_group",
        "is_active",
    )
    list_filter = (
        "email",
        "date_joined",
        "blood_group",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "blood_group",
                    "date_of_birth",
                    "is_active",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "blood_group",
                    "date_of_birth",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)

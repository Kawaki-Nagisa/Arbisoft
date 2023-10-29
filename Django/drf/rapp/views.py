from rest_framework import permissions, status, viewsets
from .models import CustomUser
from rest_framework.response import Response
from .serializers import (
    RegistrationSerializer,
    CustomDetailSerializer,
    CustomBasicSerializer,
    LoginSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API viewset for listing and creating CustomUser instances.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomBasicSerializer
    permission_classes = [permissions.AllowAny]


class UserRegisterationViewSet(viewsets.GenericViewSet):
    """
    An endpoint for the client to create a new User.
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle user registration.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginViewSet(viewsets.GenericViewSet):
    """
    An endpoint to authenticate existing users using their email and password.
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle user login.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomDetailSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)


class UserLogoutViewSet(viewsets.GenericViewSet):
    """
    An endpoint to log out an authenticated user.
    """

    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        """
        Handle user logout.
        """
        try:
            request.session.flush()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"message": "Internal server error."},
            )


class UserViewSet(viewsets.ModelViewSet):
    """
    Get and update user information.
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CustomDetailSerializer

    def get_object(self):
        return self.request.user


# class UserRegistrationView(View):
#     """
#     View for user registration.
#     """

#     def get(self, request):
#         """
#         Display the registration form.
#         """
#         return render(request, "rapp/templates/signup.html")

#     def post(self, request):
#         """
#         Handle user registration form submission.
#         """
#         registration_data = {
#             "email": request.POST["email"],
#             "password": request.POST["password"],
#             "re_password": request.POST["re_password"],
#         }

#         signup_api_url = reverse("signup-api")
#         response = requests.post(
#             request.build_absolute_uri(signup_api_url), data=registration_data
#         )

#         if response.status_code == status.HTTP_201_CREATED:
#             messages.success(request, "Registration successful. You can now log in.")
#             return redirect("login")
#         else:
#             messages.error(request, "Registration failed. Please try again.")
#             return redirect("register")

# class UserLoginView(View):
#     """
#     View for user login.
#     """

#     def get(self, request):
#         """
#         Display the login form.
#         """
#         return render(request, "rapp/templates/login.html")

#     def post(self, request):
#         """
#         Handle user login form submission.
#         """
#         login_data = {
#             "email": request.POST["email"],
#             "password": request.POST["password"],
#         }

#         login_api_url = reverse("login-api")
#         response = requests.post(
#             request.build_absolute_uri(login_api_url), data=login_data
#         )

#         if response.status_code == status.HTTP_200_OK:
#             user_data = response.json()
#             access_token = user_data.get("tokens", {}).get("access")
#             refresh_token = user_data.get("tokens", {}).get("refresh")
#             if access_token:
#                 request.session["access_token"] = access_token
#                 request.session["refresh_token"] = refresh_token

#             request.session["user_id"] = user_data.get("id")

#             profile_response = requests.get(
#                 request.build_absolute_uri(reverse("profile")),
#                 headers={
#                     "Authorization": f"Bearer {access_token}",
#                     "Content-Type": "application/json",
#                 },
#             )

#             if profile_response.status_code == status.HTTP_200_OK:
#                 return redirect("profile")
#             else:
#                 messages.error(request, "Failed to retrieve profile data.")
#                 return redirect("login")

#         else:
#             messages.error(request, "Login failed. Please try again.")
#             return redirect("login")

# class UserLogoutView(View):
#     """
#     View for user logout.
#     """

#     permission_classes = (permissions.IsAuthenticated,)

#     def get(self, request):
#         """
#         Display the logout page.
#         """
#         return render(request, "rapp/templates/logout.html")

#     def post(self, request):
#         """
#         Handle user logout.
#         """
#         logout_api_url = reverse("logout-api")
#         access_token = request.session.get("access_token")
#         response = requests.post(
#             request.build_absolute_uri(logout_api_url),
#             headers = {
#             "Authorization": f"Bearer {access_token}",
#             "Content-Type": "application/json",
#         }
#         )
#         if response.status_code == status.HTTP_204_NO_CONTENT:
#             messages.success(request, "You have been logged out.")
#             return redirect("login")
#         else:
#             messages.error(request, "Logout Failed.")
#             return redirect("profile")

# class UserProfileView(View):
#     """
#     View for user profile.
#     """

#     def get(self, request):
#         """
#         Display the user profile.
#         """
#         if not request.user.is_authenticated:
#             messages.error(request, "You need to log in to view/edit your profile.")
#             return redirect("login")

#         user_api_url = reverse("profile-api")

#         access_token = request.session.get("access_token")
#         headers = {
#             "Authorization": f"Bearer {access_token}",
#             "Content-Type": "application/json",
#         }

#         response = requests.get(
#             request.build_absolute_uri(user_api_url), headers=headers
#         )

#         if response.status_code == 200:
#             user_data = response.json()
#             return render(
#                 request, "rapp/templates/profile.html", {"user_data": user_data}
#             )
#         else:
#             messages.error(request, "Failed to fetch user data.")
#             return redirect("login")

# class UserProfileUpdateView(View):
#     """
#     View for updating user profile.
#     """

#     def get(self, request):
#         """
#         Display the edit profile form.
#         """
#         if not request.user.is_authenticated:
#             messages.error(request, "You need to log in to view/edit your profile.")
#             return redirect("login")

#         user_api_url = reverse("profile-api")

#         access_token = request.session.get("access_token")
#         headers = {
#             "Authorization": f"Bearer {access_token}",
#             "Content-Type": "application/json",
#         }

#         response = requests.get(
#             request.build_absolute_uri(user_api_url), headers=headers
#         )

#         if response.status_code == 200:
#             user_data = response.json()
#             return render(
#                 request, "rapp/templates/edit-profile.html", {"user_data": user_data}
#             )
#         else:
#             messages.error(request, "Failed to fetch user data.")
#             return redirect("login")

#     def post(self, request):
#         """
#         Handle user profile update form submission.
#         """
#         if not request.user.is_authenticated:
#             messages.error(request, "You need to log in to view/edit your profile.")
#             return redirect("login")

#         user_api_url = reverse("profile-api")

#         access_token = request.session.get("access_token")
#         headers = {
#             "Authorization": f"Bearer {access_token}",
#             "Content-Type": "application/json",
#         }

#         user_data = {
#             "first_name": request.POST.get("first_name"),
#             "last_name": request.POST.get("last_name"),
#             "email": request.POST.get("email"),
#             "date_of_birth": request.POST.get("date_of_birth"),
#             "is_superuser": request.POST.get("is_superuser"),
#             "is_active": request.POST.get("is_active"),
#         }

#         response = requests.put(
#             request.build_absolute_uri(user_api_url), json=user_data, headers=headers
#         )

#         if response.status_code == 200:
#             user_data = response.json()
#             form = CustomDetailSerializer(request.POST, instance=user_data)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Profile updated successfully.")
#                 return redirect("profile")
#             else:
#                 messages.error(request, "Invalid form data. Please correct the errors.")
#         else:
#             messages.error(request, "Failed to fetch user data.")
#         return redirect("profile")

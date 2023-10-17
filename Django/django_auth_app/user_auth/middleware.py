"""
Custom middleware for Basic Authentication.

This middleware provides basic authentication for views in case the user is not already authenticated.
It checks for the presence of the 'Authorization' header in the request, extracts the email and password
from the header, and attempts to authenticate the user with these credentials.

Attributes:
    get_response (function): The callable that represents the next middleware or view in the chain.
"""


from django.contrib.auth import authenticate
from .utils import chk_basic_auth


class BasicMiddleware:
    """
    Middleware class for Basic Authentication.

    This middleware class is responsible for providing basic authentication for views if the user is not already authenticated.
    It checks for the presence of the 'Authorization' header in the request, extracts the email and password from the header,
    and attempts to authenticate the user with these credentials.

    Args:
        get_response (function): The callable that represents the next middleware or view in the chain.

    Attributes:
        get_response (function): The callable that represents the next middleware or view in the chain.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Process the incoming request.

        If the request user is not authenticated and 'Authorization' header is present, attempts basic authentication.
        If authentication is successful, the user is set as the authenticated user for the request.

        Args:
            request (HttpRequest): The incoming request.

        Returns:
            HttpResponse: The response generated by the view or subsequent middleware.
        """
        if not request.user.is_authenticated:
            if "HTTP_AUTHORIZATION" in request.META:
                email, password = chk_basic_auth(request.META["HTTP_AUTHORIZATION"])
                user = authenticate(email=email, password=password)
                if user:
                    request.user = user

        response = self.get_response(request)
        return response

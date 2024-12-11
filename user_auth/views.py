from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# All views here
def user_login(request):
    """Renders the login page for the user.

    :param request: HttpRequest object

    :return: Returns the login.html template.
    """
    return render(request, "login.html")


def authenticate_user(request):
    """User authentication view with POST requests.
    User returned to login page if authentication fails.

    :param request: HttpRequest object
    :param username: Stores the username from the post information in the HTTP
        request.
    :param password: Stores the password from the post information in the HTTP
        request.
    :param user: Authenticates the user with the username and password.
        Returns None if authentication fails.

    :return: Returns the login.html template with an error message if
        authentication fails. Otherwise, redirects to the login_success view.
    """
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username = username, password = password)
    if user is None:
        return render(request, "login.html",
        {"error": "Invalid username or password"})
    else:
        login(request, user)
        return redirect("user_auth:login_success")


@login_required(login_url = "/user_auth")
def show_success(request):
    """Restricted view for authenticated users. Renders a success page on login.

    :param request: HttpRequest object
    
    :return: Returns the success.html template with the username of the
        authenticated user.
    """
    return render(request, "success.html",
    {"username": request.user.username})


@login_required(login_url = "/user_auth")
def logout_user(request):
    """Restricted view that logs out the user.

    :param request: HttpRequest object
    """
    logout(request)


def logged_out(request):
    """Renders a custom logged out confirmation page.

    :param request: HttpRequest object

    :return: Returns the logged_out.html template.
    """
    return render(request, "logged_out.html")

    # NOTE:  Assistance with getting the default LOG OUT success page changed
    # in SETTINGS.PY, to the custom template, was obtained from user Girik1105
    # at StackOverflow:
    # https://stackoverflow.com/questions/68698970/how-can-i-change-django-default-logout-success-template

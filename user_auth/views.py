from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    '''
    Renders the login page for the user.
    '''
    return render(request, "login.html")


def authenticate_user(request):
    '''
    User authentication view with POST requests.
    User returned to login page if authentication fails.
    '''
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
    '''
    Restricted view for authenticated users. Renders a success page on login.
    '''
    return render(request, "success.html",
    {"username": request.user.username})

@login_required(login_url = "/user_auth")
def logout_user(request):
    '''
    Restricted view that logs out the user.
    '''
    logout(request)

    # NOTE: Assistance with correctly using the logout view was obtained from
    # Django documentation:
    # https://docs.djangoproject.com/en/5.1/topics/auth/default/#:~:text=To%20log%20out%20a%20user,Redirect%20to%20a%20success%20page.

def logged_out(request):
    '''
    Renders a custom logged out confirmation page.
    '''
    return render(request, "logged_out.html")

    # NOTE:  Assistance with getting the default LOG OUT success page changed
    # in SETTINGS.PY, to the custom template, was obtained from user Girik1105
    # at StackOverflow:
    # https://stackoverflow.com/questions/68698970/how-can-i-change-django-default-logout-success-template

    
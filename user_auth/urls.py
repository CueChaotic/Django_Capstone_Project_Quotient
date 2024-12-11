from django.urls import path
from . import views

app_name = "user_auth"
"""
App name. Used for easy referencing in templates.
"""

urlpatterns = [
    path("", views.user_login, name = "login"),
    path("login_user/", views.authenticate_user, name = "login_user"),
    path("login_success/", views.show_success, name = "login_success"),
    path("logout/", views.logout_user, name = "logout"),
    path("logout_success/", views.logged_out, name = "logout_success"),
]
"""
URLs for the user authorisation app.
The first path displays the initial login page.
The second path is the user authentication function.
The third path displays a success page on login.
The fourth path is the user logout process.
The final path displays a logout confirmation page.
"""

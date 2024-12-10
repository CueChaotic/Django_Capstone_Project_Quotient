from django.urls import path
from . import views

app_name = "user_auth"

urlpatterns = [
    path("", views.user_login, name = "login"),
    path("login_user/", views.authenticate_user, name = "login_user"),
    path("login_success/", views.show_success, name = "login_success"),
    path("logout/", views.logout_user, name = "logout"),
    path("logout_success/", views.logged_out, name = "logout_success"),
]


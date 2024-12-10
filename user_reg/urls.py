from django.urls import path
from . import views

app_name = "user_reg"

urlpatterns = [
    path("", views.register, name="register_user"),
    path("registration_success/", views.register_success, name="reg_success"),
]


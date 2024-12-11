from django.urls import path
from . import views

app_name = "user_reg"
"""App name. Used for easy referencing in templates.
"""

urlpatterns = [
    path("", views.register, name="register_user"),
    path("registration_success/", views.register_success, name="reg_success"),
]
"""URLs for the user registration app.
The first path displays the registration form.
The second path displays a success message after registration after processing
the form data.
"""

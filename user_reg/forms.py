from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User registration form class
class UserRegistrationForm(UserCreationForm):
    """Captures additional user information over and above the default fields
    provided by the UserCreationForm class.

    :param UserCreationForm: A form class that creates a new user.
    :param first_name: A CharField that captures the user's first name.
        Limited to 150 characters and is required.
    :param last_name: A CharField that captures the user's last name.
        Limited to 150 characters and is required.
    :param email: An EmailField that captures the user's email address.
        Limited to 150 characters and is required.
    """
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=150, required=True)

    class Meta:
        """Defines the model and the fields to be used in the form.
    
        :param model: Uses the User model from the Django authentication system.
        :param fields: A list of fields to be used in the form.
        """
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1",
                  "password2"]

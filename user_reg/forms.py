from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User registration form class
class UserRegistrationForm(UserCreationForm):
    '''
    Captures additional user information over and above the default fields
    provided by the UserCreationForm class.
    '''
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1",
                  "password2"]


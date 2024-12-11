from django.forms import ModelForm
from .models import *

# Forum and Discussion forms:
class CreateInForum(ModelForm):
    """Form that pulls in the Forum model and excludes the user field in the
    Meta class.

    :param ModelForm: Django form that is used to create a form from a model.
    """
    class Meta:
        """Defines the model and excludes the user field.

        :param model: Uses the Forum model from models.py in the forum app.
        :param exclude: Excludes the user field from the form.
        """
        model = Forum
        exclude = ["user"]


class CreateInDiscussion(ModelForm):
    """Form that pulls in the Discussion model and excludes the user field in
    the Meta class.

    :param ModelForm: Django form that is used to create a form from a model.
    """
    class Meta:
        """Defines the model and excludes the user field.

        :param model: Uses the Discussion model from models.py in the forum app.
        :param exclude: Excludes the user field from the form.
        """
        model = Discussion
        exclude = ["user"]

# NOTE: Above code to build a discussion forum sourced (before changes) from
# DataFlair:
# https://data-flair.training/blogs/discussion-forum-python-django/

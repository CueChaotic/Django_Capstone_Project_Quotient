from django.forms import ModelForm
from .models import *

# Forum and Discussion forms:
class CreateInForum(ModelForm):
    '''
    Form that pulls in the Forum model and excludes the user field (the user
    field is pulled in directly in the view).
    '''
    class Meta:
        model = Forum
        exclude = ["user"]
 
class CreateInDiscussion(ModelForm):
    '''
    Form that pulls in the Discussion model and excludes the user field.
    '''
    class Meta:
        model = Discussion
        exclude = ["user"]

# NOTE: Above code to build a discussion forum sourced (before changes) from
# DataFlair:
# https://data-flair.training/blogs/discussion-forum-python-django/



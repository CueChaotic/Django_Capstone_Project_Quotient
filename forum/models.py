from django.db import models
from django.contrib.auth.models import User

# My models

class Forum(models.Model):
    """
    The Forum model encapsulates the data for the forum.
    Forum topics will remain even if users are deleted, for archival purposes.
    """
    user = models.ForeignKey(User, null=True, on_delete = models.SET_NULL)
    topic = models.CharField(max_length = 300)
    description = models.CharField(max_length = 1000, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    
    def __str__(self):
        '''
        Returns the string representation of the forum, which is the topic.
        '''
        return str(self.topic)

class Discussion(models.Model):
    '''
    The Discussion model encapsulates data for the discussion within the
    forum.
    Discussions will remain even if users are deleted, for archival purposes.
    '''
    user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    forum = models.ForeignKey(Forum, blank = True, on_delete = models.CASCADE)
    discuss = models.CharField(max_length = 1000)
 
    def __str__(self):
        '''
        Returns the string value of the discussion, being the forum it belongs
        to.
        '''
        return str(self.forum)
    
# NOTE: Above code to build a discussion forum sourced (before changes) from
# DataFlair:
# https://data-flair.training/blogs/discussion-forum-python-django/


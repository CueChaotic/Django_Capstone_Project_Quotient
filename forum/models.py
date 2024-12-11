from django.db import models
from django.contrib.auth.models import User

# My models

class Forum(models.Model):
    """The Forum model encapsulates the data for the forum. Forum topics will
    remain even if users are deleted, for archival purposes.

    :param models.Model: Django model that is used to create a model from a
        database.
    :param user: Defines the field parameters for the user, which is a
        ForeignKey relationship with the Django User model.
    :param topic: Defines the field parameters for the topic, which is a
        CharField with a maximum length of 300 characters.
    :param description: Defines the field parameters for the description,
        which is a CharField with a maximum length of 1000 characters.
    :param date_created: Defines the field parameters for the date_created,
        which is a DateTimeField that is automatically set when a new forum
        topic is created.
    """
    user = models.ForeignKey(User, null=True, on_delete = models.SET_NULL)
    topic = models.CharField(max_length = 300)
    description = models.CharField(max_length = 1000, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    
    def __str__(self):
        """Returns the string representation of the forum, which is the topic.

        :return: The topic of the forum.
        :rtype: str
        """
        return str(self.topic)


class Discussion(models.Model):
    """The Discussion model encapsulates data for the discussion within the
    forum. Discussions will remain even if users are deleted, for archival
    purposes.

    :param models.Model: Django model that is used to create a model from a
        database.
    :param user: Defines the field parameters for the user, which is a
        ForeignKey relationship with the Django User model.
    :param forum: Defines the field parameters for the forum, which is a
        ForeignKey relationship with the Forum model.
    :param discuss: Defines the field parameters for the discuss, which is a
        CharField with a maximum length of 1000 characters.
    """
    user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    forum = models.ForeignKey(Forum, blank = True, on_delete = models.CASCADE)
    discuss = models.CharField(max_length = 1000)
 
    def __str__(self):
        """Returns the string value of the discussion, being the forum it belongs
        to.

        :return: The forum of the discussion.
        :rtype: str
        """
        return str(self.forum)
    
# NOTE: Above code to build a discussion forum sourced (before changes) from
# DataFlair:
# https://data-flair.training/blogs/discussion-forum-python-django/

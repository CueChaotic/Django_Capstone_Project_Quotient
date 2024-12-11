from django.urls import path
from . import views

app_name = 'disc_forum'
"""App name for the forum app. Used for easy referencing in templates.
"""

# URLs here:
urlpatterns = [
    path('', views. forum_page, name='forum_page'),
    path('addInForum/', views.addInForum, name='addInForum'),
    path('addInDiscussion/', views.addInDiscussion, name='addInDiscussion'),
]
"""URLs for the forum app.
The first path is the main forum page.
The second path is for adding a new forum topic.
The third path is for adding a new discussion/comment.
"""

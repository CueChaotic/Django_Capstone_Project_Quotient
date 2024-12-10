from django.urls import path
from . import views

app_name = 'disc_forum'

# URLs here:
urlpatterns = [
    path('', views. forum_page, name='forum_page'),
    path('addInForum/', views.addInForum, name='addInForum'),
    path('addInDiscussion/', views.addInDiscussion, name='addInDiscussion'),
]


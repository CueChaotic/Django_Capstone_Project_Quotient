from django.urls import path
from . import views

app_name = 'front_page'
"""
App name for the forum app. Used for easy referencing in templates.
"""

# URLs here:
urlpatterns = [
    path('', views.front_page, name='home_page')
]

"""
URLs for the front page.
Only one path is needed for the front page.
"""

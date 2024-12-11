from django.urls import path
from . import views

app_name = 'front_page'
"""App name. Used for easy referencing in templates.
"""

# URLs here:
urlpatterns = [
    path('', views.front_page, name='home_page')
]
"""URL for the front page. Only one path is needed for the front page.
"""

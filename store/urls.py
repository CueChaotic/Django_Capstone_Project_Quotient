from django.urls import path
from . import views

app_name = "store"
"""App name. Used for easy referencing in templates.
"""

# URLs here:
urlpatterns = [
    path("", views.store_page, name="store_page")
]
"""URL for the store page. Only one path is needed.
"""

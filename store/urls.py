from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("", views.store_page, name="store_page")
]


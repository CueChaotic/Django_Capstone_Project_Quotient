from django.urls import path
from . import views

app_name = 'front_page'

# URLs here:
urlpatterns = [
    path('', views.front_page, name='home_page')
]


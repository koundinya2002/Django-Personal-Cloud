from django.urls import path
from . import views
from .views import UserRegistrationView

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
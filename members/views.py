from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# from .forms import UserRegistrationForm


# Create your views here.
def landing(request):
    return render(request, 'registration/landing.html')


class UserRegistrationView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

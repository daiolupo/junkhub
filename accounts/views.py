from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = "registration/profile.html"

class ProfileUpdateView(UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy("home")
    template_name = "registration/profile_edit.html"

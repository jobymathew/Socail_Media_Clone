from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from . import forms
# Create your views here.

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class SignUp(CreateView):
    form_class = forms.UserCreateFrom
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
    

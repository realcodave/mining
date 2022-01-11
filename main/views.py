from django.shortcuts import render
from django.views import generic
from .models import User
# Create your views here.


class HomeView(generic.ListView):
    template_name = "index.html"
    model = User

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

# Create your views here.

class PWMainView(ListView): #default view of main page
    model = Project
    template_name = 'projects.html'


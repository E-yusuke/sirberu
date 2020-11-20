from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):# Create your views here.
    template_name = "user/index.html"

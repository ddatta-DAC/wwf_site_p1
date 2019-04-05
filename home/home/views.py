from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

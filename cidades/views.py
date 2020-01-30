from django.views.generic import DetailView
from django.shortcuts import render
from cidades.models import City

# Create your views here.

class CityDetailView(DetailView):
    """
    Cities Detail View
    """

    template_name = 'cidades/city-detail.html'
    model = City


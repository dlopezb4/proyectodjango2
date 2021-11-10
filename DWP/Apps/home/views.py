from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

class ClientesView(TemplateView):
    template_name = "clientes.html"

class ContactoView(TemplateView):
    template_name = "contacto.html"

class ConectarView(TemplateView):
    template_name = "conectar.html"
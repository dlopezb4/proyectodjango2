from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"

class ClientesView(TemplateView):
    template_name = "clientes.html"

class ContactoView(TemplateView):
    template_name = "contacto.html"

def home(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'login/index.html', context)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
        else:
            form = UserCreationForm()

        context = {'form' : form}
        return render(request, 'home:login:register.html', context)


from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Superhero


class HeroListView(ListView):
    model = Superhero
    template_name = 'hero.html'

class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'hero_detail.html'

class HeroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'hero_add.html'
    fields = ['name', 'identity', 'body', 'strength', 'weakness']

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'hero_edit.html'
    fields = ['name', 'identity', 'body', 'strength', 'weakness']

class HeroDeleteView(LoginRequiredMixin, DeleteView): 
    model = Superhero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero')

class BasePage(TemplateView):
    template_name = "superhero_theme.html"

class AboutPage(TemplateView):
    template_name = 'about.html'

class HomePage(TemplateView):
    template_name = 'home.html'

class ProfilePage(TemplateView):
    template_name = 'profile.html'
from .views import AboutPage, BasePage, HomePage, ProfilePage, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView, HeroDeleteView
from django.urls import path
from . import views

urlpatterns = [
    path('hero', HeroListView.as_view(), name='hero'),
    path('<int:pk>/', HeroDetailView.as_view(), name='hero_detail'),
    path('hero/new/', HeroCreateView.as_view(), name='hero_add'),
    path('hero/<int:pk>/delete/', 
        HeroDeleteView.as_view(), name='hero_delete'),
    path('hero/<int:pk>/edit/',
        HeroUpdateView.as_view(), name='hero_edit'),
    path('about', AboutPage.as_view()),
    path('home', HomePage.as_view()),
    path('profile', ProfilePage.as_view()),
    path('', HomePage.as_view()),

] 
"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.http import HttpResponse
from django.urls import path


def home_page_view(request):
    return HttpResponse("<h1>World's Simplest Home Page</h1>")

def about_page_view(request):
    return HttpResponse("<h1>World's Simplest About Page</h1>")

urlpatterns = [
    path('', home_page_view),
    path('about', about_page_view),
]

"""ctrl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from database import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('page/<int:page_id>/', views.index),
    path('news/<int:news_id>/', views.news),
    path('team/<int:team_id>/', views.team),
    path('team/<int:team_id>/page/<page_id>/', views.team),
    path('search/<keyword>/', views.search),
    path('search/<keyword>/page/<page_id>/', views.search),
]

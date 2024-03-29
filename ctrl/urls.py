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
from django.urls import path, re_path
from django.conf.urls import handler404, url

from django.conf import settings
from django.views import static

from database import views

handler404 = "database.views.page_not_found"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('page/<int:page_id>/', views.index),
    path('news/<int:news_id>/', views.news),
    path('team/<int:team_id>/', views.team),
    path('team/<int:team_id>/page/<int:page_id>/', views.team),
    path('search/<keyword>/', views.search),
    path('search/<keyword>/page/<int:page_id>/', views.search),
    path('bot/', views.bot_admin),
    path('about/', views.about),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name = 'static'),
]

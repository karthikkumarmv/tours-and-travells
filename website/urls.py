"""website URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [ 
    path('', include('newwebsite.urls')),
    path('index', include('newwebsite.urls')),
    path('about', include('newwebsite.urls')),
    path('destinations', include('newwebsite.urls')),
    path('destinations2', include('newwebsite.urls')),
    path('destinations3', include('newwebsite.urls')),
    path('destinations4', include('newwebsite.urls')),
    path('destinations5', include('newwebsite.urls')),
    path('dest6', include('newwebsite.urls')),
    path('bk', include('newwebsite.urls')),
    path('email', include('newwebsite.urls')),
    path('honey', include('newwebsite.urls')),
    path('outstion', include('newwebsite.urls')),
    path('tour', include('newwebsite.urls')),
    path('airport', include('newwebsite.urls')),
    path('contact', include('newwebsite.urls')),
    path('sm1', include('newwebsite.urls')),
    path('sm2', include('newwebsite.urls')),
    path('sm3', include('newwebsite.urls')),
    path('sm4', include('newwebsite.urls')),
    path('sm5', include('newwebsite.urls')),
    path('sm6', include('newwebsite.urls')),
    path('sm7', include('newwebsite.urls')),
    path('sm8', include('newwebsite.urls')),
    path('sm9', include('newwebsite.urls')),
    path('sm10', include('newwebsite.urls')),
    path('sm11', include('newwebsite.urls')),
    path('tbl', include('newwebsite.urls')),
    path('elements', include('newwebsite.urls')),
    path('news', include('newwebsite.urls')),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

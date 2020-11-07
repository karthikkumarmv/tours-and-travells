from django.contrib import admin
from django.urls import path, include
from  .  import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('destinations', views.destinations, name='destinations'),
    path('destinations2', views.destinations2, name='destinations2'),
    path('destinations3', views.destinations3, name='destinations3'),
    path('destinations4', views.destinations4, name='destinations4'),
    path('destinations5', views.destinations5, name='destinations5'),
    path('dest6', views.dest6, name='dest6'),
    path('bk', views.bk, name='bk'),
    path('email', views.email, name='email'),
    path('tbl', views.tbl, name='tbl'),
    path('sm1', views.sm1, name='sm1'),
    path('sm2', views.sm2, name='sm2'),
    path('sm3', views.sm3, name='sm3'),
    path('sm4', views.sm4, name='sm4'),
    path('sm5', views.sm5, name='sm5'),
    path('sm6', views.sm6, name='sm6'),
    path('honey', views.honey, name='honey'),
    path('outstion', views.outstion, name='outstion'),
    path('airport', views.airport, name='airport'),
    path('contact', views.contact, name='contact'),
    path('tour', views.tour, name='tour'),
    path('sm7', views.sm7, name='sm7'),
    path('sm8', views.sm8, name='sm8'),
    path('sm9', views.sm9, name='sm9'),
    path('sm10', views.sm10, name='sm10'),
    path('sm11', views.sm11, name='sm11'),
    path('elements', views.elements, name='elements'),
    path('news', views.news, name='news'),
    ]
    

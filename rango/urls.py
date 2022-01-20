# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:10:06 2022

@author: Iacovos
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('about/', views.about, name= 'about')
    ]
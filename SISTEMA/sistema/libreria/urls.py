from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.principal),
    path('contactanos',views.contactanos,name='contactanos'),
]
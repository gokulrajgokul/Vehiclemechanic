from django.shortcuts import render,redirect
from django.contrib import admin
from django.urls import path, include   

# Create your views here.
def home(request):
    return render(request, 'base.html')


def home(request):
    return render(request,'home.html')
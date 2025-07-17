from django.shortcuts import render,redirect
from django.contrib import admin
from django.urls import path, include   


def home(request):
    return render(request,'home.html')


def base(request):
    return render(request,'base.html')
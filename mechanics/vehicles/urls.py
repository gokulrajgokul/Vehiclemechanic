from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('signout', views.signout, name='signout'),
    path('addmech', views.addmech, name='addmech'),
]
from django.contrib import admin
from django.urls import path
from appTwo import views
from django.urls import include

urlpatterns = [
    path('',views.users,name='users'),

]

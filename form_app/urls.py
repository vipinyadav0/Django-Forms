from django.contrib import admin
from django.urls import path
from form_app import views
from form_app.forms import NameForm

urlpatterns = [
    path('', views.index),
    path('formpage', views.NameForm, name=NameForm),
]
from django.urls import path
from . import views

#Url coonfig
urlpatterns = [
    path('hello/',views.say_hello)
]
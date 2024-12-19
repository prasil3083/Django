from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# requst and rsponse (request handler)

def say_hello(request):
    return render(request,"hello.html" , { 'name' : 'Prasil' })
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contact_me(request):
    return HttpResponse('Welcome to the Contact Me page!!')
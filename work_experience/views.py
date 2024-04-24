from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def work_experience(request):
    if request.method == 'GET':
        return HttpResponse('GETting to the work experience page')
    else:
        return HttpResponse('POSTing the work experience page')
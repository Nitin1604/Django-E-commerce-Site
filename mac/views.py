# Folder Path : DjangoCourse\mac\mac\views.py

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

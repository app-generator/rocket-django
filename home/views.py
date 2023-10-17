from django.shortcuts import render


from .models import *

def index(request):

  context = {
    'segment': 'dashboard',
  }
  return render(request, "pages/dashboard/index.html", context)

def starter(request):

  context = {}
  return render(request, "starter.html", context)
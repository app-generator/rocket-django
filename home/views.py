from django.shortcuts import render


from .models import *

def index(request):

  context = {
    'segment': 'dashboard',
  }
  return render(request, "dashboard/index.html", context)

@login_required(login_url='/users/signin/')
def starter(request):

  context = {}
  return render(request, "pages/starter.html", context)

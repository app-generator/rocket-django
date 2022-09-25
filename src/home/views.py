# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def index(request):

    return render(request, "admin/index.html")

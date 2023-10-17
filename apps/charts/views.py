from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'segment'  : 'charts',
        'parent'   : 'apps',
    }
    return render(request, 'pages/apps/charts.html', context)

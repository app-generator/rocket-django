from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def datatables(request):
  context = {
    'segment'  : 'datatables',
    'parent'   : 'apps',
  }
  return render(request, 'pages/apps/datatables.html', context)
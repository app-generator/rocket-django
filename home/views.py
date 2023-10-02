from django.http import HttpResponse

# HOMEpage
def index(request):
    return HttpResponse('Hello from <a target="_blank" href="https://github.com/app-generator/rocket-django">Rocket Django</a>')

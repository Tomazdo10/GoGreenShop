from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index paige"""

    return render(request, "home/index.html")

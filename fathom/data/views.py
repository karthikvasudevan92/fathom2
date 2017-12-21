from django.shortcuts import render
from .models import Unit

# Create your views here.
def dash(request):
    return render(request, 'data/dash.html', {})

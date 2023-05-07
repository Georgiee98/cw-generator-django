from django.shortcuts import render
from .models import Profile
# Create your views here.

def accept(request):
    # if request.method == 'POST':

    return render(request, 'pdf/accept.html')
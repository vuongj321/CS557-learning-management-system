from django.shortcuts import render
from django.contrib.auth.decorators import login_not_required

# Create your views here.
@login_not_required
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')
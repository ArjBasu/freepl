# Create your views here.
from django.shortcuts import render
from simulator.models import users

def landing(request):
    return render(request,"index.html",{
        "title":"Welcome to Freepl",
                                 })

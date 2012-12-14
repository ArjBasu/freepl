# Create your views here.
from django.shortcuts import render

def landing(request):
    return render(request,"index.html",{
        "title":"Welcome to Freepl",
                                 })

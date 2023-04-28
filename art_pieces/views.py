from django.http import HttpResponse
from django.shortcuts import render
from .models import ArtPiece

# Create your views here.


def index(request):
    pieces = ArtPiece.objects.all()
    return render(request, "index.html", {'pieces': pieces})


def a4(request):
    return render(request, 'a4_page.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

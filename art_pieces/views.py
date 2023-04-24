from django.http import HttpResponse
from django.shortcuts import render
from .models import ArtPiece

# Create your views here.


def index(request):
    pieces = ArtPiece.objects.all()
    return render(request, "index.html", {'pieces': pieces})

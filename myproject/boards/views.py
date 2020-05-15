from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def goodbye(request):
    return HttpResponse('<h1>Goodbye, World!</h1>')
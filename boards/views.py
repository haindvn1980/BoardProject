from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})


def board_topics(request, boards_id):
    board = Board.objects.get(pk=boards_id)
    return render(request, 'boards/topics.html', {'board': board})

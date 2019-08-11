from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Board


# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})


def board_topics(request, boards_id):
    board = Board.objects.get(pk=boards_id)
    return render(request, 'boards/topics.html', {'board': board})


def new_topic(request, boards_id):
    board = get_object_or_404(Board, pk=boards_id)
    #nếu ấn vòa nút post, mình sẽ lấy giá trị và lưu và db
    if request.mothod=="POST":
        # lấy dữ liệu về subject
        subject = request.POST['subject']
        # lấy dữ liệu về message
        message = request.POST['message']
        # lấy ra user đang log in hiện tại
        user = User.object.first()



    return render(request, 'boards/new_topic.html', {'board': board})

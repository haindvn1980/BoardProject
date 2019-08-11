from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm


# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})


def board_topics(request, boards_id):
    board = Board.objects.get(pk=boards_id)
    return render(request, 'boards/topics.html', {'board': board})


def new_topic(request, boards_id):
    board = get_object_or_404(Board, pk=boards_id)
    user = User.objects.first()  # TODO: get the currently logged in user
    # nếu ấn vòa nút post, mình sẽ lấy giá trị và lưu và db
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter_by = user
            topic.save()
            # lưu vào bảng Post
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', boards_id=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})

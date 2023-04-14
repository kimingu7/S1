from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    boards = Board.objects.all().order_by('-created_at')
    context = {
        'boards': boards
    }
    return render(request, 'boards/index.html', context)

@require_http_methods(["GET", "POST"])
def detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        if request.user == board.author:
            board.delete()
        return redirect('boards:index')

    comments = board.comments.all()
    comment_form = CommentForm()
    
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'boards/detail.html', context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user == board.author:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                form.save()
                return redirect('boards:detail', pk=board.pk)
        else:
            form = BoardForm(instance=board)
    else :
        return redirect('boards:detail', board.pk)
    context = {
        'board': board,
        'form': form,
    }        
    return render(request, 'boards/update.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/create.html', context)

@require_http_methods(["POST"])
def comment(request, board_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.author = request.user
            comment.save()
            return redirect('boards:detail', board.pk)

@require_http_methods(["POST"])
def comment_detail(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        if request.user == comment.author:
            comment.delete()
        return redirect('boards:detail', board_pk)
    
@require_http_methods(["POST"])
def likes(request, board_pk):
    if request.user.is_authenticated:
        board = Board.objects.get(pk=board_pk)
        if board.like_users.filter(pk=request.user.pk).exists():
            board.like_users.remove(request.user)
        elif board.dislike_users.filter(pk=request.user.pk).exists():
            board.dislike_users.remove(request.user)
            board.like_users.add(request.user)
        else:
            board.like_users.add(request.user)
        return redirect('boards:index')
    return redirect('accounts:login')

@require_http_methods(["POST"])
def dislikes(request, board_pk):
    if request.user.is_authenticated:
        board = Board.objects.get(pk=board_pk)
        if board.dislike_users.filter(pk=request.user.pk).exists():
            board.dislike_users.remove(request.user)
        elif board.like_users.filter(pk=request.user.pk).exists():
            board.like_users.remove(request.user)
            board.dislike_users.add(request.user)
        else:
            board.dislike_users.add(request.user)
        return redirect('boards:index')
    return redirect('accounts:login')
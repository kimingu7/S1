from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todos/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {'form': form}
    return render(request, 'todos/create.html', context)

@login_required
def complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todos:index')

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.author:
            todo.delete()
            return redirect('todos:index')
    return redirect('todos:index')
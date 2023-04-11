from django.shortcuts import render, redirect
from .forms import QuestionForm, CommentForm
from .models import Question, Comment
from random import choice
# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'eithers/index.html', context)

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eithers:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'eithers/create.html', context)

def detail(request, pk):
    question = Question.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = question.comment_set.all()
    context = {
        'question': question,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)

def comment(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.question = question
            comment.save()
            return redirect('eithers:detail', pk)
    else:
        form = CommentForm()
    context = {'form' : form}
    return render(request, 'eithers/detail.html', context)

def random(request):
    random_question = choice(Question.objects.all())
    return redirect('eithers:detail', pk=random_question.pk)

def update(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('eithers:detail', question.pk)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form, 'question': question}
    return render(request, 'eithers/update.html', context)

def delete(request, pk):
	question = Question.objects.get(pk=pk)
	if request.method == 'POST':
		question.delete()
		return redirect('eithers:index')
	else :
		return redirect('eithers:detail', question.pk)

def comment_delete(request, question_pk, comment_pk):
     comment = Comment.objects.get(pk=comment_pk)
     comment.delete()
     return redirect('eithers:detail', question_pk)
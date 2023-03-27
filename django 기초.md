```bash
python -m venv venv # 가상환경 만들기

source venv/Scripts/activate # 가상환경 활성화

$ pip install django==3.2.18 # django 설치

$ django-admin startproject <pjt_name> . # 프로젝트 생성

$ python manage.py startapp <app_name> # 앱 생성

$ python manage.py runserver # 서버 시작

settings.py의 installed_apps에 '<app_name>', 추가 # 앱 경로 추가
<pjt_name>의 urls.py에 urlpatterns에 path('<app_name>/', views.index), 추가
<app_name>의 views.py에 from django.http import HttpResponse
def index(request):
	return HttpResponse("") 추가
	
templates 폴더 생성할 경우
def index(request):
	return render(request, '<app_name>/index.html') # index.html은 templates/<app_name> 안에 있어야 함
```

Throw

```django
urls.py에서
urlpatterns = [
	...,
	path('throw/', views.throw),
]

views.py에서
def throw(request):
	return render(request, 'throw.html')
	
throw.html에서
{% extends 'base.html' %}

{% block content %}
	<h1>Throw</h1>
	<form action='/catch/' method='GET'>
        <label for='message'>Throw</label>
        <input type='text' id='message' name='message'>
        <input type='submit'>
	</form>
	<a href="/index/">back</a>
{% endblock content %}
```

Catch

```django
urls.py에서

urlpattenrs = [
	...,
	path('catch/', views.catch),
]

views.py에서

def catch(request):
	message = request.GET.get('message')
	context = {
		'message' : message,
	}
	return render(request, 'catch.html', context)

catch.html에서
{% extends 'base.html' %}

{% block content %}
	<h1>Catch</h1>
	<h2>{{message}}</h2>
	<a href="/throw/">Back</a>
{% endblock content %}
```

Database

```bash
models.py에서
class Article(models.Model):
	title = models.CharField(max_length=10) # CharField는 max_length가 존재
	content = models.TextField() # TextField는 max_length가 필요하지 않음
	
$ python manage.py makemigrations
$ python manage.py migrate
$ pip install ipython, django-extensions
$ python manage.py shell_plus

settings.py에서
INSTALLED_APPS에 'django_extensions' 추가

Articles.objects.all() # 전부 조회

CREATE
1.
article = Article()
article.title = '<title>' # 타이틀
article.content = '<content>' # 콘텐츠
article.save() # Article에 저장

2. 
article = Article(title='<title>', content='<content>')
article.save() # Article에 article 저장

3.
Article.objects.create(title='<title>', content='<content>')

READ ( pk 대신 id를 사용해도 가능 )
1. 
article = Article.objects.get(pk=<n>)
article.title
article.content

2.
Article.objects.get(pk=<n>).title
Article.objects.get(pk=<n>).content

UPDATE

article = Article.objects.get(pk=<n>)
article.title = '<title>'
article.save()

DELETE

article = Article.objects.get(pk=<n>)
article.delete()
```



```django
$ python manage.py createsuperuser (관리자 계정 생성)

admin.py에서

from django.contrib import admin
from .models import Article

admin.stie.register(Article)
```

```django
사전 준비
base.html에서
bootstarp CDN 생성
! 후 head와 body에 각각 경로 복붙

settings.py의 'TEMPLATES'에서
'DIRS' : [BASE_DIR / 'templates',],

articles의 urls.py에서
from django.urls import path

app_name = 'articles'
urlpatterns = [
	path('', views.index, name='index')
]

crud의 urls.py에서
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('articles/', include('articles.urls')),
]

articles의 views.py에서
def index(request):
	return render(request, 'articles/index.html')
	
index.html에서
{% extends 'base.html' %}

{% block content %}
	<h1>Articles</h1>
{% endblock content %}

models.py에서
from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextField()
	
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
```



```django
READ (전체 게시글 조회)
articles의 vies.py에서
from .models import Article

def index(request):
	articles = Article.objects.all()
	context = {
		'articles' : articles,
	}
	return render(request, 'articles/index.html', context)

index.html에서
{% extends 'base.html' %}

{% block content %}
	<h1>Articles</h1>
	<hr>
	{% for article in articles %}
		<p>글 번호 : {{ article.pk }}</p>
		<p>글 제목 : {{ article.title }}</p>
		<p>글 내용 : {{ article.content }}</p>
		<hr>
	{% endfor %}
{% endblock content %}

READ (개별 게시글 조회)

articles의 urls.py에서
urlpatterns = [
	...,
	path('<int:pk>/', views.detail, name='detail'),
]
articles의 views.py에서

def detail(request, pk):
	article = Article.objects.get(pk=pk)
	context = {
		'article' : article,
	}
	return render(request, 'articles/detail.html', context)

detail.html에서
{% extends 'base.html' %}

{% block content %}
	<h2>DETAIL</h2>
	<h3>{{ article.pk }} 번째 글</h3>
    <hr>
	<p>제목: {{ article.title }}</p>
	<p>내용: {{ article.content }}</p>
	<p>작성 시각: {{ article.created_at }}</p>
	<p>수정 시각: {{ article.updated_at }}</p>
	<hr>
	<a href="{% url 'articles:index' %}">[BACK]</a>
{% endblock content %}

index.html에서
{% extends 'base.html' %}

{% block content %}
	<h1>Articles</h1>
	{% for article in articles %}
		<p>글 번호: {{ article.pk }}</p>
		<a href="{% url 'articles:detail' article.pk %}">
			<p>글 제목: {{ article.title }}</p>
		</a>
		<p>글 내용: {{ article.content }}</p>
		<hr>
	{% endfor %}
{% endblock content %}

CREATE (new를 사용)
articles의 urls.py에서
urlpatterns = [
	...,
	path('new/', views.new, name='new'),
	path('create/', views.create, name='create'),
]
articles의 view.py에서
def new(request):
    return render(request, 'articles/new.html')

def create(request):
	title = request.GET.get('title')
	content = request.GET.get('content')
	생성방식 3가지
	1.
	article = Article()
	article.title = title
	article.content = content
	article.save()
	
	2.
	article = Article(title=title, content=content)
	article.save()
	
	3.
	Article.objects.create(title=title, content=content)
	return redirect('articles:detail', article.pk)
	
new.html에서
{% extends 'base.html' %}

{% block content %}
	<h1>NEW</h1>
	<form action="{% url 'articles:create' %}" method="GET">
		<label for="title">Title: </label>
		<input type="text" name="title"><br>
		<label for="content">Content: </label>
		<textarea name="content"></textarea><br>
		<input type="submit">
	</form>
	<hr>
	<a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}

index.html에서
{% extends 'base.html' %}

{% block content %}
	<h1>Articles</h1>
	<a href="{% url 'articles:new'%}">NEW</a>
{% endblock content %}

GET : R 역할
POST : C, U, D 역할

POST method 적용

new.html에서
{% extends 'base.html' %}

{% block content %}
	<h1>NEW</h1>
	<form action="{% url 'articles:create' %}" method="POST">
		{% csrf_token %}
		<label for="title">Title: </label>
		<input type="text" name="title"><br>
		<label for="content">Content: </label>
		<textarea name="content"></textarea><br>
		<input type="submit">
	</form>
	<hr>
	<a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}

views.py
def create(request):
	title = request.POST.get('title')
	content = request.POST.get('content')
	...

DELETE

articles의 urls.py에서
urlpatterns = [
	...
	path('<int:pk>/delete/', views.delete, name='delete'),
]

views.py에서
def delete(request, pk):
	article = Article.objects.get(pk=pk)
	article.delete()
	return redirect('articles:index')

detail.html에서

{% extends 'base.html' %}

{% block content %}
	...
	<form action="{% url 'articles:delete' article.pk %}" method="POST">
		{% csrf_token %}
		<input type="submit" value="DELETE">
	</form>
	<a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}

UPDATE (edit)

articles의 urls.py에서
urlpatterns = [
	...
	path('<int:pk>/edit/', views.edit, name='edit'),
]

views.py에서
def edit(request, pk):
	article = Article.objects.get(pk=pk)
	context = {
		'article' : article,
	}
	return render(request, 'articles/edit.html', context)

edit.html에서

{% extends 'base.html' %}

{% block content %}
	<h1>EDIT</h1>
	<form action="{% url 'articles:edit' %}" method="POST">
		{% csrf_token %}
		<label for="title">Title: </label>
		<input type="text" name="title" value="{{ article.title }}"><br>
		<label for="content">Content: </label>
		<textarea name="content">{{ article.content }}</textarea><br>
		<input type="submit">
	</form>
	<hr>
	<a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}

detail.html에서
{% extends 'base.html' %}

{% block content %}
	<h2>DETAIL</h2>
	<h3>{{ article.pk }} 번째 글</h3>
    <hr>
	<p>제목: {{ article.title }}</p>
	<p>내용: {{ article.content }}</p>
	<p>작성 시각: {{ article.created_at }}</p>
	<p>수정 시각: {{ article.updated_at }}</p>
	<hr>
	<a href="{% url 'articles:edit' %}">[BACK]</a><br>
	<form action="{% url 'articles:delete' article.pk %}" method="POST">
		{% csrf_token %}
		<input type="submit" value="DELETE">
	</form>
	<a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}

UPDATE (update)

articles의 urls.py에서
urlpatterns = [
	...
	path('<int:pk>/update/'), views.update, name='update'),
]

views.py에서
def update(request, pk):
	article = Article.objects.get(pk=pk)
	article.title = request.POST.get('title')
	article.content = request.POST.get('content')
	article.save()
	return redirect('articles:detail', article.pk)
	
edit.html에서

{% extends 'base.html' %}

{% block content %}
	<h1>EDIT</h1>
	<form action="{% url 'articles:update' article.pk %}" method="POST">
		{% csrf_token %}
		<label for="title">Title: </label>
		<input type="text" name="title" value="{{ article.title }}"><br>
		<label for="content">Content: </label>
		<textarea name="content">{{ article.content }}</textarea><br>
		<input type="submit">
	</form>
	<hr>
	<a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```

Handling HTTP requests

```
Create
views.py에서
def create(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		article = Article(title=title, content=content)
		article.save()
		return redirect('articles:detail', pk=article.pk)
	else :
		return render(request, 'articles/create.html')
		
이 때, views.py와 urls.py에서 new를 삭제하고, index.html과 new.html의 new를 create로 변경

Update
views.py에서
def update(request, pk):
	article = Article.objects.get(pk=pk)
	if request.method == 'POST':
		article.title = request.POST.get('title')
		article.content = request.POST.get('content')
		article.save()
		return redirect('articles:detail', pk=article.pk)
	else :
		context = {'article': article}
		return render(request, 'articles/update.html', context)
이 떄, views.py와 urls.py에서 edit을 삭제하고, detail.html과 edit.html의 edit을 update로 변경

DELETE
views.py에서
def delete(request, pk):
	article = Article.objects.get(pk=pk)
	if request.method == 'POST':
		article.delete()
		return redirect('articles:index')
	else :
		return redirect('articles:detail', article.pk)

detail.html에서
...
<form action="{% url 'articles:delete' article.pk %}" method="POST">
...

# render와 redirect의 차이
render 주어진 정보대로 화면 구성
redirect urls로 다시 연결 (views를 다시 실행)

# return 유무에 따른 차이
redirect url만 반환 (이동하지 않음)
return redirect HTTP Response까지 반환 (실제로 이동함)
```

Django Form Class

```django
forms.py에서
from django import forms

class ArticleForm(forms.Form):
	title = forms.CharField(max_length=<n>)
	content = forms.CharField()

# content = forms.CharField(widget=forms.Textarea)를 통해 widget 적용
	
views.py에서
from .forms import ArticleForm
...
def create(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		article = Article(title=title, content=content)
		article.save()
		return redirect('articles:detail', pk=article.pk)
	else :
		form = ArticleForm()
		context = {'form': form}
		return render(request, 'articles/create.html', context)
		
create.html에서
{% extends 'base.html' %}

{% block content %}
  <h1>글작성</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```

ModelForm

```django
forms.py에서
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

# exclude=('content',)를 사용할 경우 content 제거 가능

save() method에서 instance의 여부에 따라 Create와 Update를 구분 가능

views.py에서
def create(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save()
			return redirect('articles:detail', article.pk)
	else :
		form = ArticleForm()
		
    context = {'form': form}
    return render(request, 'articles/create.html', context)
    
def update(request, pk):
	article = Article.objects.get(pk=pk)
	if request.method == 'POST':
		form = ArticleForm(request.POST, instance=article)
		if form.is_valid():
			form.save()
			return redirect('articles:detail', article.pk)
	else :
		form = ArticleForm(instance=article)
	
	context = {'form': form, 'article': article}
	return render(request, 'articles/update.html', context)

update.html에서
{% extends 'base.html' %}

{% block content %}
  <h1>글수정</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>

  <hr>
  <a href="{% url 'articles:index' %}">돌아가기</a>
{% endblock content %}
```


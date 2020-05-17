from django.shortcuts import render, redirect
from .models import Article 
# Create your views here.
def index_show(request):
  movie_articles = Article.objects.filter(category="movie").count()
  drama_articles = Article.objects.filter(category="drama").count()
  entertain_articles = Article.objects.filter(category="entertain").count()
  return render(request, 'index.html', {
    'movie_articles':movie_articles, 
    'drama_articles':drama_articles, 
    'entertain_articles':entertain_articles
    })

def movie_show(request):
  movie_article_title = Article.objects.filter(category="movie")
  return render(request, 'movie.html', {'movie_article_title':movie_article_title})

def drama_show(request):
  drama_article_title = Article.objects.filter(category="drama")
  return render(request, 'drama.html', {'drama_article_title':drama_article_title})

def entertain_show(request):
  entertain_article_title = Article.objects.filter(category="entertain")
  return render(request, 'entertain.html', {'entertain_article_title':entertain_article_title})

def detail(request, clicked):
  article = Article.objects.get(pk=clicked)
  return render(request, 'detail.html', {'article':article})

def new(request):
  if request.method == 'POST':
    print(request.POST)
    new_article = Article.objects.create(
      title = request.POST['title'],
      content = request.POST['content'],
      category = request.POST['category']
    )
    return redirect('detail', clicked=new_article.pk)
  else:
    return render(request, 'new.html')
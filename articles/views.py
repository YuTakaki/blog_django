from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def articles(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, "articles/article_lists.html", {'articles' : articles})

def article_details(request, id):
    article = Article.objects.get(id = id)
    return render(request, "articles/details.html", {'article' : article})

@login_required(login_url="/sign-in")
def create_article(request):
    if request.method == 'POST':
        if "id" in request.POST:
            instance = Article.objects.get(id=request.POST.get("id"))
            instance.body = request.POST.get("body")
            instance.title = request.POST.get("title")
            instance.save()
            return redirect('articles:all')
        else: 
            form = forms.CreateArticle(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('articles:all')

    else:
        if "id" in request.GET:
            blog = Article.objects.get(id=request.GET.get("id"))
            form = forms.CreateArticle(instance=blog)
        else:
            form = forms.CreateArticle()
    return render(request, 'articles/create_article.html', {'form': form})

@login_required(login_url="/sign-in")
def delete_article(request, id):
    Article.objects.filter(id = id).delete()
    return redirect('articles:all')
from django.shortcuts import render
from django.views.generic import ListView
from blog import models

# class ArticleListView(ListView):
#     model = Article
#
#     def get_queryset(self):
#         return Article.objects

def home_page(request):
    article = models.Article.objects.all
    return render(request, 'blog.html', context={'article_list':article})

def post_page(request, post_id):
    context = {
        'post': models.Article.objects.get(id=post_id)
    }
    return render(request, "single.html", context)
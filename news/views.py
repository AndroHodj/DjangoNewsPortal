from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = 'heading'
    template_name = 'news.html'
    context_object_name = 'news'


class OneNews(DetailView):
    model = Post
    ordering = 'heading'
    template_name = 'new.html'
    context_object_name = 'onenews'


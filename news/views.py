from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .forms import NewsForm, ArticlesForm
from django.urls import reverse_lazy
from .filters import NewsFilter
from .resources import news, article


class NewsList(ListView):
    model = Post
    ordering = 'heading'
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class OneDetail(DetailView):
    model = Post
    ordering = 'heading'
    template_name = 'news_detail.html'
    context_object_name = 'onenews'


class ArticlesCreate(CreateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = article
        return super().form_valid(form)


class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = news
        return super().form_valid(form)


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_articles_delete.html'
    success_url = reverse_lazy('news_list')


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'



from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post
from .forms import NewsForm
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = 'heading'
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
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


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = Post.CATEGORIES
        return super().form_valid(form)


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'news_articles_delete.html'
    success_url = reverse_lazy('news_list')


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')


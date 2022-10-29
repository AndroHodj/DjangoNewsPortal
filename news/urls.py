from django.urls import path
from .views import OneDetail, NewsList, NewsCreate, NewsDelete, NewsUpdate


urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>/', OneDetail.as_view(), name='news_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]

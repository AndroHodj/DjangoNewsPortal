from django.urls import path
# Импортируем созданное нами представление
from .views import OneNews, NewsList


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>/', OneNews.as_view())
]

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating_post'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.user.comment_set.aggregate(commentRating=Sum('rating_comment'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.rating_author = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return f'{self.user.username}'


class Category(models.Model):
    category_name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Post(models.Model):
    NEWS = 'NW'
    ARTICLES = 'AR'
    CATEGORIES = [
        (NEWS, 'Новость'),
        (ARTICLES, 'Статья'),
    ]

    article_or_news = models.CharField(max_length=2, choices=CATEGORIES, default=NEWS)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    heading = models.CharField(max_length=150)
    txt = models.TextField(max_length=200)
    rating_post = models.IntegerField(default=0)

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        if len(self.txt) > 124:
            return f'{self.txt[:124]}...'
        return f'{self.txt}'

    def __str__(self):
        return f'{self.heading}:{self.txt}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}'

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    txt_comment = models.TextField()
    datetime_in = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

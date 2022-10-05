#### from django.contrib.auth.models import User
#### from news.models import *
#### from news.resources import *


Создать двух пользователей (с помощью метода User.objects.create_user('username')).
================================
#### user1 = User.objects.create_user("Andro")
#### user2 = User.objects.create_user("Kate")


Создать два объекта модели Author, связанные с пользователями.
================================
#### Author.objects.create(user = user1)
#### Author.objects.create(user = user2)


Добавить 4 категории в модель Category.
================================
#### Category.objects.create(category_name = 'Sport')
#### Category.objects.create(category_name = 'History')
#### Category.objects.create(category_name = 'News')
#### Category.objects.create(category_name = 'Article')


Добавить 2 статьи и 1 новость.
================================
#### Post.objects.create(article_or_news = 'AR', author = author1, heading = 'Title', txt = 'text')
#### Post.objects.create(article_or_news = 'AR', author = author1, heading = 'Title', txt = 'text')
#### Post.objects.create(author = author, heading = 'Title', txt = 'text')


Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
================================
#### Post.objects.get(id=1).category.add(Category.objects.get(id=1))
#### Post.objects.get(id=1).category.add(Category.objects.get(id=2))
#### Post.objects.get(id=2).category.add(Category.objects.get(id=3))
#### Post.objects.get(id=2).category.add(Category.objects.get(id=2))
#### Post.objects.get(id=3).category.add(Category.objects.get(id=4))
#### Post.objects.get(id=3).category.add(Category.objects.get(id=1))


Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
================================
#### Comment.objects.create(comment_post=Post.objects.get(pk=1),comment_user=Author.objects.get(pk=1).user, txt_comment = 'Very cool story')
#### Comment.objects.create(comment_post=Post.objects.get(pk=2),comment_user=Author.objects.get(pk=1).user, txt_comment = 'Not Bad')
#### Comment.objects.create(comment_post=Post.objects.get(pk=2),comment_user=Author.objects.get(pk=2).user, txt_comment = 'Good job')
#### Comment.objects.create(comment_post=Post.objects.get(pk=3),comment_user=Author.objects.get(pk=1).user, txt_comment = 'Interesting article')


Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
================================
#### Comment.objects.get(pk=1).like()
#### Comment.objects.get(pk=1).like()
#### Comment.objects.get(pk=1).like()
#### Comment.objects.get(pk=2).like()
#### Comment.objects.get(pk=1).rating_comment
#### Post.objects.get(pk=1).rating_post


Обновить рейтинги пользователей.
================================
#### user1 = Author.objects.get(pk=1)
#### user1.update_rating()
#### user1.rating_author


Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
================================
#### s = Author.objects.order_by('-rating_author')
#### for i in s:
#### ...    i.rating_author
#### ...    i.user.username
    
    
Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.   
================================
#### p = Post.objects.order_by('-rating_post')
#### for i in p[:1]:
#### ...     i.time_in
#### ...     i.author.user
#### ...     i.rating_post
#### ...     i.heading
#### ...     i.preview()    


Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
================================
#### Post.objects.all().order_by('-rating_post')[0].comment_set.values('datetime_in', 'comment_user', 'rating_comment', 'txt_comment')

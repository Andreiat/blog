from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    '''Модель статей'''
    class Meta():
        db_table = 'post'
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["create"]

    title = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст статьи", max_length=1500)
    image = models.ImageField("Изображение", upload_to="post/", blank=True)
    create = models.DateTimeField("Создан", auto_now_add=True)
    update = models.DateTimeField("Обновлено", auto_now=True)
    moder = models.BooleanField("Модерация", default=False)

    def __str__(self):
        return self.title

class CommentPost(models.Model):
    '''Модель комметариев'''
    class Meta():
        db_table = 'comments'
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    user = models.ForeignKey(User, verbose_name="Пользователь")
    post = models.ForeignKey(Post, verbose_name="Статья")
    text = models.TextField("Текст комментария", max_length=500)
    created = models.DateTimeField("Добавлен", auto_now_add=True)
    moder = models.BooleanField("Модерация", default=False)

from os import name
from django.db import models

class Navbar(models.Model):
    name = models.CharField(verbose_name="Названия", max_length=50)
    url = models.CharField(verbose_name="URL", max_length=50)
    position = models.IntegerField(verbose_name="Позиция")
    posted   = models.BooleanField(verbose_name="Опубликованно", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Меню сайта"
        verbose_name_plural = "Элементы меню"

#Категории постов
class Category(models.Model):
    name        = models.CharField(verbose_name="Имя категориии", max_length=20)
    description = models.TextField(verbose_name="Описание")
    slug        = models.SlugField(verbose_name="Сылка", max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Категория"
        verbose_name_plural = "Категории"

#Пост
class Post(models.Model):
    title    = models.CharField(verbose_name="Заголовок статьи", max_length=100,)
    img      = models.ImageField(verbose_name="Картинка поста", upload_to="images/")
    content  = models.TextField(verbose_name="Описание")
    date     = models.DateField(verbose_name="Дата публикации", auto_now=True)
    slug     = models.SlugField(verbose_name="Сылка", max_length=160, unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    posted   = models.BooleanField(verbose_name="Опубликованно", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = "Пост"
        verbose_name_plural = "Посты"
   
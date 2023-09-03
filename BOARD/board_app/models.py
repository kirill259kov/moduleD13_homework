from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.authorUser)


CATEGORIES = [
    ('T','Танки'),
    ('HM','Хилы'),
    ('DD','ДД'),
    ('TrM','Торговцы'),
    ('GM','Гилдмастеры'),
    ('QG','Квестгиверы'),
    ('FM','Кузнецы'),
    ('LM','Кожевники'),
    ('PM','Зельевары'),
    ('WM','Мастера заклинаний'),
]


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    category = models.CharField(verbose_name='Категория', max_length=3, choices=CATEGORIES, default='T')
    title = models.CharField(max_length=128)
    content = CKEditor5Field('Text', blank=True, null=True, config_name='extends')


class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    responseAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    isAccepted = models.BooleanField(null=True)

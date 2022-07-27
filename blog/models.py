from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField('Загаловок', max_length=255)
    slug = models.SlugField('Ссылка', unique=True)
    image = models.ImageField('Картинка', null = True, blank = True, upload_to = 'category_img/')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField('Загаловок', max_length=255)
    image = models.ImageField('Картинка', null = True, blank = True, upload_to = 'post_img/')
    text = models.TextField('Содержание')
    view = models.IntegerField('Просмотры', default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория')
    slug = models.SlugField('Ссылка', unique=True)
    date = models.DateTimeField('Дата публикации', default=timezone.now )
    pub = models.BooleanField('Публикация', default=False)
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_link(self):
        return reverse('post_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField('Текст комментария')
    date = models.DateTimeField('Дата', default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор коментария')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = 'Пост')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.user.username + '|' + self.post.title
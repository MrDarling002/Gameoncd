from email.mime import image
from pyexpat import model
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField('Загаловок', max_length=255,db_index=True)
    slug = models.SlugField('Ссылка', unique=True,db_index=True)
    image = models.ImageField('Картинка', null = True, blank = True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField('Загловок', max_length=255)
    image = models.ImageField('Картинка', null = True, blank = True)
    text = models.TextField('Содержание')
    view = models.IntegerField('Просмотры', default=0)
    category = models.ManyToManyField(Category,verbose_name='Категория')
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

class Game_category(models.Model):
    title = models.CharField('Категория игры', max_length=255,db_index=True)
    image = models.ImageField('Картинка', null = True, blank = True)
    slug = models.SlugField('Ссылка', unique=True,db_index=True)
    


    class Meta:
        verbose_name = 'Категория игры'
        verbose_name_plural = 'Категории игр'

    def __str__(self):
        return self.title

class Game_text(models.Model):
    title = models.CharField('Название платформы', max_length=255)
    text=models.TextField('Текст платформы')
    youtube= models.CharField('Ссылка на видео', max_length=255, db_index=True, blank=True )

class Game_dev(models.Model):
    title = models.CharField('Название платформы игры', max_length=255,db_index=True)
    image = models.ImageField('Картинка', null = True, blank = True) 
    category=models.ManyToManyField(Game_category,verbose_name='Категория игр входящие в платформу')
    
 

    slug = models.SlugField('Ссылка', unique=True,db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Платформа игры'
        verbose_name_plural = 'Платформы игр'


class Game(models.Model):
    title = models.CharField('Название игры', max_length=255)
    game_category=models.ManyToManyField(Game_category,verbose_name='Категория игры')
    game_dev = models.ManyToManyField(Game_dev,verbose_name='Категория платформы игры')
    image = models.ImageField('Главная Картинка', null = True, blank = True)
    youtube=models.CharField('Ссылка на трейлер', max_length=255)
    system= models.TextField('Системные требования') 
    plot=models.TextField('Сюжет')
    effects= models.TextField('Визуальные эффекты')
    sound= models.TextField('Звук')
    features= models.TextField('Функции')
    image1=models.ImageField('Картинка 1', null = True, blank = True)
    image2=models.ImageField('Картинка 2', null = True, blank = True)
    image3=models.ImageField('Картинка 3', null = True, blank = True)
    slug = models.SlugField('Ссылка', unique=True,db_index=True)
    date = models.DateTimeField('Дата публикации', default=timezone.now )
    pub = models.BooleanField('Публикация', default=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обзор игр'
        verbose_name_plural = 'Обзоры игр'

    def get_game(self):
        return reverse('game_url', kwargs={'slug':self.slug})
    
    def get_category(self):
        return reverse('game_category_url', kwargs={'slug':self.slug})









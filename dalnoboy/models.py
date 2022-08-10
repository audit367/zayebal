from django.db import models
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    file=models.FileField(
        upload_to='video',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        verbose_name='Видео'
    )
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Stranic(models.Model):
    str_title=models.CharField(max_length=70, verbose_name='Страничка')
    title=models.CharField(max_length=70, verbose_name='Оглавление')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    url = models.URLField(verbose_name='ссылки')
    email=models.EmailField(verbose_name='email')
    url_ad=models.URLField(verbose_name='адрес ссылка')
    title_ad=models.TextField(verbose_name='адрес')
    id_n=models.CharField(max_length=20, verbose_name='Номер')
    file = models.FileField(
        upload_to='video',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        verbose_name='Видео'
    )

    def __str__(self):
        return self.title
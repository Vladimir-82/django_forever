from django.db import models
#БД

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True) # не обязательное поле blank=True
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self): #возвращает команду News.objects.all() к строковому типу
        return self.title

    class Meta: # изменяем внешний интерфейс
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']  # сортировка


from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields import DateTimeField

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_at']

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
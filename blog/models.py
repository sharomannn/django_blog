from django.db import models


class Categery(models.Model):
    # objects = None
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('Название', max_length=255, blank=True, default='',
                             unique=True)
    summary = models.CharField('Короткое описание', max_length=255, blank=True,
                               default='', unique=True)
    full_text = models.TextField(' Oписание',
                                 help_text='Подсказка для понимания',
                                 blank=True)
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано')
    created = models.DateTimeField('Создан', auto_now_add=True, db_index=True)
    updated = models.DateTimeField('Обновлён', auto_now=True)
    categery = models.ManyToManyField(Categery, verbose_name='Categeries',
                                      blank=True, related_name='categery')

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Список статей'
        ordering = ('created',)

    def __str__(self):
        return self.title

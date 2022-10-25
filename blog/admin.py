from django.contrib import admin
from blog import models
@admin.register(models.Article)
class Article(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_filter = ('title',)

@admin.register(models.Categery)
class Categery(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

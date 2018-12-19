from django.contrib import admin
from .models import Article, Comment

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

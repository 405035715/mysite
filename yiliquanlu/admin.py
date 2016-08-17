from django.contrib import admin

from .models import Article,News




 
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['content']}),
    ]
admin.site.register(Article, ArticleAdmin)

class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['news_title']}),
        (None,               {'fields': ['news_time']}),
        (None,               {'fields': ['news_content']}),  
    ]
admin.site.register(News, NewsAdmin)
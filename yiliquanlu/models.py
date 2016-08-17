from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader import *
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    content = RichTextField('正文')
    
class News(models.Model):
    news_title = models.CharField(max_length=30)
    news_time = models.DateTimeField()
    news_content = RichTextUploadingField()
    




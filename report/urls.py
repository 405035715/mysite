from django.conf.urls import url
from . import views

app_name = 'report'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'cke/$', views.testCkeditor, name='testCkeditor'),
]
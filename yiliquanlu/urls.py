from django.conf.urls import url
from . import views

app_name = 'yiliquanlu'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'cke/$', views.testCkeditor, name='testCkeditor'),
]
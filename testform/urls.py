from django.conf.urls import url
from . import views

app_name = 'testform'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'name/$', views.get_name, name='get_name'),
]
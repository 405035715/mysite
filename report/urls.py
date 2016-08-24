from django.conf.urls import url
from . import views

app_name = 'report'

urlpatterns = [
    url(r'^$', views.patientlist, name='patientlist'),
    url(r'report/$', views.report, name='report'),
    #url(r'cke/$', views.testCkeditor, name='testCkeditor'),
]
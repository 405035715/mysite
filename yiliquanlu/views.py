from django.shortcuts import render,get_object_or_404
from django.template.context_processors import request
from .models import News




def index(request):
    context = {
        # 'latest_question_list': latest_question_list,
    }
    return  render(request,'yiliquanlu/index.html',context)

def testCkeditor(request):
    context = {
               'news':    News.objects.get(pk=1),
               }
   
    return  render(request,'yiliquanlu/testCKEditor.html',context)
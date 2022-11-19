from django.views.generic import TemplateView
from datetime import datetime
from mainapp import models
from django.shortcuts import get_object_or_404

class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"

class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs): 
        # Get all previous data 
        context=super().get_context_data(**kwargs) 
        # Create your own data 
        context["news_title"] = "Громкий новостной заголовок"
        context[ "news_preview" ] = "Предварительное описание, которое заинтересует каждого" 
        context["range"] = range(5)
        context["datetime_obj"] =datetime.now()
        context["news_qs"] = models.News.objects.all()[:10]
        return context

class NewsWithPaginatorView(NewsPageView):
    
    def get_context_data(self,page, **kwargs):
        context=super().get_context_data(page = page,**kwargs) 
        context["page_num"] = page
        return context

class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"

class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"

class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
# Create your views here.

class NewsPageDetailView(TemplateView): 
    emplate_name = "mainapp/news_detail.html" 

    def get_context_data(self, pk=None, **kwargs): 
        context = super().get_context_data(pk=pk, **kwargs) 
        context["news_object"] = get_object_or_404(models.News, pk=pk) 
        return context
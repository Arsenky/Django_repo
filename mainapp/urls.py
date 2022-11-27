"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.decorators.cache import cache_page
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [ 
    path("", views.MainPageView.as_view(), name="main_page"), 
    path("news/", views.NewsListView.as_view(), name="news"), 
    path("news/create/", views.NewsCreateView.as_view(), name="news_create"), 
    path( "news/<int:pk>/detail", views.NewsDetailView.as_view(), name="news_detail", ), 
    path( "news/<int:pk>/update", views.NewsUpdateView.as_view(), name="news_update", ), 
    path( "news/<int:pk>/delete", views.NewsDeleteView.as_view(), name="news_delete", ), 
    path("courses/", cache_page(60 * 5)(views.CoursesListView.as_view()), name="courses"), 
    path( "courses/<int:pk>/", views.CoursesDetailView.as_view(), name="courses_detail", ), 
    path("course_feedback/",views.CourseFeedbackFormProcessView.as_view(),name="course_feedback",),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"), 
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    path("log_view/", views.LogView.as_view(), name="log_view"),
    path("log_download/", views.LogDownloadView.as_view(), name="log_download"),
    ]
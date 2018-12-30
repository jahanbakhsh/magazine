from django.urls import path
from news import views as news_views

urlpatterns =[
    path('', news_views.index, name="index"),
    path("news/", news_views.RetrivNews, name="retrive_news"),
]
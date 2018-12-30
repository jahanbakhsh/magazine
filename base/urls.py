from django.urls import path
from base import views as base_views

urlpatterns =[
    path('subscription',base_views.subscription , name="subscription"),
    path('login' , base_views.Newslogin , name='login'),
    path('logout' , base_views.Newslogout , name='logout'),
    path('register' , base_views.NewsRegister , name='register'),
    path('message' , base_views.ContactUsMessage , name='contact_us_mesage'),
    path('contact_us', base_views.ContactUs, name='contact_us'),
]
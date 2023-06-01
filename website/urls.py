from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('user', views.user, name='user'),
    path('tool', views.home, name='tool'),
    path('webex', views.webex, name='webex'),
    path('insertWebexUser', views.insertWebexUser, name='insertWebexUser'),
]
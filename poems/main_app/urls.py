from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('home/', views.home, name='home'),
 path('about/', views.about, name ='about'),
 path('accounts/signup/', views.signup, name='signup'),
 path('index/', views.index, name ='index'),
 path('index/create', views.PoeCreate.as_view(), name='poes_create'),
]
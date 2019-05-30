from django.urls import path
from . import views

app_name = 'fashionapp'

urlpatterns =[
    path('', views.index, name='index'),
    path('(?P<clothe_id>[0-9]+)/', views.details, name='detail'),
    path('create_clothe/', views.create_clothe, name='create_clothe'),
    path('(?P<clothe_id>[0-9]+)/delete_clothe',views.delete_clothe, name='delete_clothe'),
    path('register/',views.register,name = 'register'),
    path('login/', views.login_user, name ='login_user'),
    path('logout/', views.logout_user, name = 'logout_user'),



]


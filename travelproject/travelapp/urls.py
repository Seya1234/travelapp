from . import views
from django.urls import path
app_name='travelapp'
urlpatterns = [

    path('',views.demo,name='demo'),
    path('add/',views.addition,name='addition'),
    path('home/',views.home,name='home'),


]
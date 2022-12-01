from . import views
from django.urls import path

app_name = 'credentials'

urlpatterns = [

    path('register', views.register, name='register'),
    path('l-in', views.login, name='login'),
    path('l-out', views.logout, name='logout')

]

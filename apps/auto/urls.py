from django.urls import path
from . import views

app_name = 'auto'
urlpatterns = [
    path('', views.home, name='index'),

]
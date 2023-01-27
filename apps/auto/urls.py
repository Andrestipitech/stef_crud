from django.urls import path
from . import views

app_name = 'auto'
urlpatterns = [
    path('', views.home, name='index'),
    path('insertar_a/', views.insertar_auto, name='crear_auto'),
    path('eliminar_a/<int:id_auto>', views.eliminar_auto, name='eliminar_auto'),

]
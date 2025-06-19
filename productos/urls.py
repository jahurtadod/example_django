from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.lista_productos, name='listar_productos'),
]

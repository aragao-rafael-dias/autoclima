from django.urls import path
from climograma import views

urlpatterns = [
    path('', views.criar_climograma, name='criar_climograma'), 
    path('criar_climograma/', views.criar_climograma, name='criar_climograma'),
    path('sucesso/', views.sucesso, name='sucesso')
]

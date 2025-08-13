# films/urls.py
from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('add/', views.add_film, name='add_film'),
    path('edit/<int:pk>/', views.edit_film, name='edit_film'),  # ← Новый путь
    path('delete/<int:pk>/', views.delete_film, name='delete_film'),
    path('', views.film_list, name='film_list'),
]
from django.urls import path

from .views import *

urlpatterns = [
    path('', index), # при обращении к главной странице подключаем метод индекс
    path('category/<int:category_id>/', get_category), # при обращении к КАТЕГОРИЯМ подключаем метод индекс
]
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'), # при обращении к главной странице подключаем метод индекс
    path('category+'
         '.0/<int:category_id>/', get_category, name='category'), # при обращении к КАТЕГОРИЯМ подключаем метод индекс
]
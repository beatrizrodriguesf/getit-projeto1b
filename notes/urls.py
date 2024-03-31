from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update_id, name='update_id'),
    path('update', views.update, name='update'),
    path('category/<str:category_name>', views.category, name='category'),
    path('tags', views.categories, name='tags'),
]
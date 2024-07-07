from django.urls import path
from .views import home_page, create_task, read_task, update_task, delete_task

urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', create_task, name='create_task'),
    path('read/<int:id>/', read_task, name='read_task'),
    path('edit/<int:id>/', update_task, name='update_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
]

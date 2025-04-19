from django.urls import path,include
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.index, name='index' ),
    path("task_list/",views.task_list, name="task_list"),
    path('add/', views.add_task, name='add_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),     # NEW
    path('delete/<int:task_id>/', views.delete_task, name='delete_task') # NEW
] 
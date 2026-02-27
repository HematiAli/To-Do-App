from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('created/', views.TaskCreate.as_view(), name='task_create'),
    path('update/<int:pk>', views.TaskUpdate.as_view(), name='task_update'),
    path('complete/<int:pk>', views.TaskComplete.as_view(), name='task_complete'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name='task_delete'),
]
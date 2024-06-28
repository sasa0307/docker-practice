from django.urls import path
from mytodo import views as mytodo
from .import views

urlpatterns = [
    path("", mytodo.index, name="index"),
    path("add/", mytodo.add, name="add"),
    path("Update_task_complite/",mytodo.Update_task_complete, name="Update_task_complite"),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
]

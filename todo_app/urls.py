
from django.urls import path
from . import views 

urlpatterns = [
   path("", views.list_todo_items),
   path("add/", views.addTodo),
   path("delete/<int:id>/",views.deleteTodo ),
   path("update/<int:id>/",views.completion ),
]
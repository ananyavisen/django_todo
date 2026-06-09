
from django.urls import path
from . import views 

urlpatterns = [
   path("", views.list_todo_items),
   path("add/", views.showContent),
   path("delete/<int:id>/",views.deleteTodo ),
]
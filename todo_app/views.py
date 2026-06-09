from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.

def list_todo_items(request):
    todos = Todo.objects.all()
    count = Todo.objects.count()
    return render(request, "todo_app/home.html" , {"todos": todos, "count": count})

def showContent(request : HttpRequest):
    content = request.POST['content'].strip()
    if(content == "" ):
        return redirect("/")
    todo = Todo(content = content)
    todo.save()
    return redirect("/")

def deleteTodo(request, id):
    todo = Todo.objects.filter(id=id)
    todo.delete()
    return redirect("/")

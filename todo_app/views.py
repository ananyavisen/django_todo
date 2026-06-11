from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.

def list_todo_items(request):
    count = Todo.objects.count()
    filter = request.GET.get("filter")
    selected_date = request.GET.get("date")
    if(filter == "done"):
        todos = Todo.objects.filter(completion = True)
    elif(filter == "pending"):
        todos = Todo.objects.filter(completion = False)
    else:
        todos = Todo.objects.all()
    
    todos = todos.filter(created_at__date = selected_date)
    
    return render(request, "todo_app/home.html" , {"todos": todos, "count": count})

def showContent(request : HttpRequest):
    content = request.POST['content'].strip()
    filter = request.GET.get("filter")
    if(content == "" ):
        return redirect("/")
    todo = Todo(content = content)
    todo.save()
    return redirect("/")

def deleteTodo(request, id):
    todo = Todo.objects.filter(id=id)
    todo.delete()
    return redirect("/")

def completion(request, id):
    todo = Todo.objects.get(id=id)
    todo.completion = not todo.completion
    todo.save()
    return redirect("/")

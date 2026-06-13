from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo
from datetime import datetime 

# Create your views here.

def list_todo_items(request):
    filter = request.GET.get("filter")
    selected_date = request.GET.get("date")
    
    todos = Todo.objects.all()

    if selected_date:
        todos = todos.filter(created_at__date=selected_date)
        display_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
    else:
        display_date = None

    if filter == "done":
        todos = todos.filter(completion=True)
    elif filter == "pending":
        todos = todos.filter(completion=False)

    count = todos.count()
    
    return render(
        request,
        "todo_app/home.html",
        {
            "todos": todos,
            "count": count,
            "date": display_date,
            "filter": filter,
        },
    )

def addTodo(request : HttpRequest):
    selected_date = request.GET.get("date")
    content = request.POST['content'].strip()
    filter = request.GET.get("filter")
    if(content == "" ):
        return redirect(f"/?date={selected_date}")
    todo = Todo(content = content)
    todo.save()
    
    if selected_date and filter:
        return redirect(f"/?date={selected_date}&filter={filter}")

    if selected_date:
        return redirect(f"/?date={selected_date}")

    return redirect("/")

def deleteTodo(request, id):
    print("Delete view called", id)
    selected_date = request.GET.get("date")
    todo = Todo.objects.filter(id=id)
    todo.delete()

    if selected_date:
        return redirect(f"/?date={selected_date}")

    return redirect("/")

def completion(request, id):
    todo = Todo.objects.get(id=id)
    todo.completion = not todo.completion
    todo.save()
    return redirect("/")

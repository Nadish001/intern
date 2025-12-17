from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        notes = request.POST['notes']
        Todo.objects.create(subject=subject, notes=notes)
        return redirect('index')
    return render(request, 'todo/form.html')

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.subject = request.POST['subject']
        todo.notes = request.POST['notes']
        todo.save()
        return redirect('index')
    return render(request, 'todo/form.html', {'todo': todo})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('index')

def view_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todo/view.html', {'todo': todo})

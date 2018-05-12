from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from todo_handler.models import Todo
from todo_handler.forms import Form_new_todo


def home(request):
    todos = Todo.objects.all()
    return render(request, 'todo_handler/home.html', {'todos': todos})


def create(request):
    if request.method == 'POST':
        form = Form_new_todo(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            deadline = form.cleaned_data['deadline']
            progress = form.cleaned_data['progress']

            new_todo = Todo(title=title, description=description,
                            deadline=deadline, progress=progress)
            new_todo.save()
            return HttpResponseRedirect('..')
    else:
        form = Form_new_todo()
        return render(request, 'todo_handler/create.html', {'form': form})


def edit_todo(request, pk):
    if request.method == 'POST':
        form = Form_new_todo(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            deadline = form.cleaned_data['deadline']
            progress = form.cleaned_data['progress']

            target = get_object_or_404(Todo, pk = pk)

            target.update_todo(title, description, deadline, progress)
            
            return HttpResponseRedirect('..')
    else:
        todo = get_object_or_404(Todo, pk=pk)
        form = Form_new_todo(instance = todo)
        return render(request, 'todo_handler/edit.html', {'todo': todo, 'form': form})

def authors(request):
    return render(request, 'todo_handler/authors.html')

def remove_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('index')


from django.shortcuts import render, redirect
from .models import Todo
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def todo_list(request):
    todos = Todo.objects.all().order_by('-added_date')
    return render(request, 'todo/index.html', {'todos': todos})

@csrf_exempt
@login_required
def add_todo(request):
    current_date = timezone.now()
    user = request.user.username
    content = request.POST["content"]
    Todo.objects.create(added_date=current_date, text=content, user=user)
    return redirect('todo_list')

@csrf_exempt
def delete_todo(request,pk):
    Todo.objects.filter(id=pk).delete()
    return redirect('todo_list')

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = UserCreationForm()

    return render(request, 'todo/register.html', {'form': form})
@csrf_exempt
def after_login(request):
    return redirect('todo_list')
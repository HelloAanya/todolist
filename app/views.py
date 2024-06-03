from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Task 
from .forms import TaskForm

def first_view(request):
    return render(request, 'first.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username already exists'})
        else:
           
            User.objects.create_user(username=username, password=password)
            return redirect('login')
    return render(request, 'signup.html')
def home_view(request):
    # Retrieve all tasks
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def create_task_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        completed = request.POST.get('completed') == 'on'  
        user_id = request.user.id 
        task = Task.objects.create(title=title, description=description, due_date=due_date, completed=completed, user_id=user_id)
        return redirect('home')
    return render(request, 'create_task.html')

def custom_logout(request):
 
    return render(request, 'first.html')

def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'update_task.html', {'form': form, 'task_id': task_id, 'task': task})
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        # Delete task logic here
        task.delete()
        return redirect('home')
    return render(request, 'delete_task.html', {'task': task})


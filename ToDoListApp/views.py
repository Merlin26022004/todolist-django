from django.shortcuts import render, redirect
from .models import Task, loginForm
from .forms import RegistrationForm, LoginForm, TaskForm, UpdateProfileForm
from django.conf import settings

def home(request):
    return render(request, 'ToDoListApp/home.html')


def dashboard(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')

    user = loginForm.objects.get(id=user_id)

    return render(request, 'ToDoListApp/dashboard.html', {'user': user})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            loginForm.objects.create(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'ToDoListApp/register.html', {'form': form})


def userloginform1(request):
    print("Login view called")
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = loginForm.objects.get(username=username, password=password)
                request.session['user_id'] = user.id
                return redirect('dashboard')
            except loginForm.DoesNotExist:
                return redirect('login')

        return redirect('login')

    return redirect('login')


def login_view(request):
    form = LoginForm()
    return render(request, 'ToDoListApp/login.html', {'form': form})

# def update_profile(request):
#     # id = request.GET.get('id')
#     # users=loginForm.objects.get(id=id)
#     # return render(request, 'ToDoListApp/profile_update.html', {'users': users})

#     if request.method == 'POST':
#         form = UpdateProfileForm(request.POST)
#         if form.is_valid():
#             return redirect('dashboard')
#     else:
#         form = UpdateProfileForm()

#     return render(request, 'ToDoListApp/profile_update.html', {'form': form})

def update_profile(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')

    user = loginForm.objects.get(id=user_id)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UpdateProfileForm(instance=user)

    return render(request, 'ToDoListApp/profile_update.html', {'form': form})


def add_task(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')   # or 'home'
    else:
        form = TaskForm()

    return render(request, 'ToDoListApp/add_task.html', {'form': form})

def send_test_email(request):
    from django.core.mail import send_mail

    send_mail(
        subject="Test Email",
        message="This is a test mail from merlin",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['mca2543@rajagiri.edu'],
        fail_silently=False,
    )

    return render(request, 'ToDoListApp/add_task.html', {'form': form})

def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'ToDoListApp/view_tasks.html', {'tasks': tasks})
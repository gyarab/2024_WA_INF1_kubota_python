from .models import Project, Profile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FeedbackForm, LoginForm, RegisterForm

def index(request):
    projects = Project.objects.order_by('-created')[:3]
    return render(request, 'leon_app/index.html', {'projects': projects})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'leon_app/projects.html', {'projects': projects})

def contact(request):
    return render(request, 'leon_app/contact.html')

def about(request):
    return render(request, 'leon_app/about.html')

def project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.project = project
            feedback.save()
            return redirect('leon_app:project', pk=project.pk)
    else:
        form = FeedbackForm()

    return render(request, 'leon_app/project.html', {'project': project, 'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('leon_app:index')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'leon_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('leon_app:index')

def settings(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'leon_app/settings.html', {'profile': profile})


# Extra stuff (not in navbar)
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('leon_app:index')
    else:
        form = RegisterForm()
    return render(request, 'leon_app/register.html', {'form': form})

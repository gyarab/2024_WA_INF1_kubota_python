from django.http import HttpResponse
from .models import Project, Feedback
from django.shortcuts import render, get_object_or_404
from .forms import FeedbackForm

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
    else:
        form = Feedback()

    return render(request, 'leon_app/project.html', {'project': project, 'form': form})
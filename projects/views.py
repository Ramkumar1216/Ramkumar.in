from django.shortcuts import render, get_object_or_404
from .models import Project

def projects_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects_list.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.exclude(slug=slug)[:3]
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'projects/project_detail.html', context)

from django.shortcuts import render
from services.models import Service
from projects.models import Project
from .models import Testimonial

def home(request):
    services = Service.objects.all()[:3]
    projects = Project.objects.all()[:3]
    testimonials = Testimonial.objects.all()[:3]
    
    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)

def about(request):
    context = {
        'profile_photo_url': '/media/profile/profile.jpg',  # Change to your actual photo filename
    }
    return render(request, 'core/about.html', context)

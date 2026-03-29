from django.shortcuts import render, get_object_or_404
from .models import Service

def services_list(request):
    """Display all available services"""
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'services/services_list.html', context)

def service_detail(request, slug):
    """Display individual service detail page"""
    service = get_object_or_404(Service, slug=slug)
    # Get all services for sidebar/comparison (optional)
    all_services = Service.objects.exclude(id=service.id)
    context = {
        'service': service,
        'all_services': all_services,
    }
    return render(request, 'services/service_detail.html', context)

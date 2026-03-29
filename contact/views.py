from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! I\'ll get back to you soon.')
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

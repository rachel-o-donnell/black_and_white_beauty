from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    View for the contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(
                request, 'Thank you for contacting us! We will get back to you by email within 24hrs.')
            return redirect('/')

    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})

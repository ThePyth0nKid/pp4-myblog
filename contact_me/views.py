from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success message
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact_me/contact.html', {'form': form | crispy})

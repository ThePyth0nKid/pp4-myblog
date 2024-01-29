from django.shortcuts import render, redirect
from contact_me.models import Contact


def admin_messages(request):
    if request.user.is_authenticated and request.user.is_superuser:
        # Angenommen, es gibt ein Feld 'created_at'
        contacts = Contact.objects.all()
        return render(request, 'admin_dashboard/admin_dashboard.html', {'contacts': contacts})
    else:
        # Umleiten, wenn der Benutzer kein Admin ist
        # Ersetzen Sie 'home' durch den Namen Ihrer Startseiten-URL
        return redirect('home')

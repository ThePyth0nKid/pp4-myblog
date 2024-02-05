from django.shortcuts import render, redirect
from contact_me.models import Contact
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import PostForm
from django.contrib import messages


@login_required
def admin_messages(request):
    """
    Displays a list of messages from the 'Contact' model for superusers.

    - If the user is a superuser, it retrieves all 'Contact' objects and displays them in the 'admin_dashboard.html' template.
    - If the user is not a superuser, it redirects them to the 'home' page.

    Args:
        request: HttpRequest object containing metadata about the request.

    Returns:
        HttpResponse object rendering the 'admin_dashboard.html' template with the list of 'Contact' objects.
    """
    if request.user.is_authenticated and request.user.is_superuser:
        # Assuming there is a 'created_at' field
        contacts = Contact.objects.all()
        return render(request, 'admin_dashboard/admin_dashboard.html', {'contacts': contacts})
    else:
        # If the user is not a superuser, redirect them to the 'home' page
        return redirect('home')


@login_required
def create_post(request):
    """
    Creates a new blog post. This view is only accessible to authenticated superusers.

    - If the request method is POST, it attempts to create a new post using the submitted form data.
    - Validates the form data, and if valid, sets the post's author to the currently logged-in user and saves the post.
    - Redirects to the 'home' page after successful post creation and shows a success message.
    - If the request method is not POST (e.g., GET), it displays an empty form for creating a new post.

    Args:
        request: HttpRequest object containing metadata about the request.

    Returns:
        HttpResponse object that renders the 'create_post.html' template with the post creation form.
    """
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                new_post = form.save(commit=False)
                # Set the post's author to the currently logged-in user
                new_post.author = request.user
                new_post.save()
                # Display a success message to the user
                messages.success(
                    request, 'The post has been successfully created!')
                # Redirect to the home page after successful post creation
                return redirect('home')
        else:
            form = PostForm()

        # Render the post creation form for GET requests or if form validation fails
        return render(request, 'admin_dashboard/create_post.html', {'form': form})
    else:
        # If the user is not authenticated or not a superuser, redirect them to the 'home' page
        messages.warning(
            request, 'You do not have permission to create a post.')
        return redirect('home')

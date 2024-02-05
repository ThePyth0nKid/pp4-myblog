from blog.models import Post
from django.shortcuts import render, redirect, get_object_or_404
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
def create_post(request, slug=None):
    """
    Create or edit a blog post using its slug. This view is only accessible to authenticated superusers.

    - If the request method is POST, it attempts to create or edit a post using the submitted form data.
    - Validates the form data, and if valid, sets the post's author to the currently logged-in user and saves the post.
    - Redirects to the post detail page after successful post creation or editing and shows a success message.
    - If the request method is not POST (e.g., GET), it displays a form for creating or editing a post, pre-filled if editing.

    Args:
        request: HttpRequest object containing metadata about the request.
        slug: Optional parameter for editing an existing post (pass the post's slug to edit).

    Returns:
        HttpResponse object that renders the 'create_post.html' template with the post creation or edit form.
    """
    post = None
    if slug:
        post = get_object_or_404(Post, slug=slug)
        if not request.user.is_superuser:
            messages.error(
                request, "You do not have permission to edit this post.")
            return redirect('post_detail', slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_or_edited_post = form.save(commit=False)
            new_or_edited_post.author = request.user
            new_or_edited_post.save()
            # Necessary for saving many-to-many relationships, if any.
            form.save_m2m()
            messages.success(request, "Post '{}' successfully updated!".format(
                new_or_edited_post.title) if post else "Post '{}' successfully created!".format(new_or_edited_post.title))
            return redirect('post_detail', slug=new_or_edited_post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'admin_dashboard/create_post.html', {'form': form, 'post': post})



@login_required
def delete_post(request, slug):
    """
    Delete a blog post using its slug. This view is only accessible to authenticated superusers.
    """
    if not request.user.is_superuser:
        messages.warning(
            request, 'You do not have permission to delete a post.')
        return redirect('home')

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'The post has been successfully deleted!')
    return redirect('home')

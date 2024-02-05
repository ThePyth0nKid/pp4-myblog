from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    # Filter and retrieve all Post objects where status equals 1
    queryset = Post.objects.filter(status=1)

    # Get the specific post by its slug, or raise a 404 error if not found
    post = get_object_or_404(queryset, slug=slug)

    # Retrieve all comments for the post, ordering them from newest to oldest
    comments = post.comments.all().order_by("-created_on")

    # Count the number of approved comments for the post
    comment_count = post.comments.count()

    # Process the form only on a POST request
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)

    # Save the comment if the form is valid
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted'
            )

    comment_form = CommentForm()

    # Render the post detail page with post data and comments
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


# This view handles comment editing functionality.
def comment_edit(request, slug, comment_id):
    """
    Handles the editing of a comment by a POST request on a specific post.

    This view function allows users to edit their comments on a blog post. It first checks if the request is a POST. 
    If so, it attempts to fetch the specific post and comment using the provided `slug` and `comment_id`. 
    It then creates a `CommentForm` instance with the POST data and the comment instance to be edited. 
    If the form is valid and the user making the request is the author of the comment, it updates the comment,
    marks it as not approved, and saves it. A success message is added to the messages framework. 
    If there are any errors, an error message is added instead.

    Parameters:
    - request (HttpRequest): The HTTP request sent to the view, containing method and POST data.
    - slug (str): The slug of the post to which the comment belongs. Used to identify the specific post.
    - comment_id (int): The ID of the comment to be edited. Used to identify the specific comment.

    Returns:
    - HttpResponseRedirect: Redirects to the detail page of the post after the comment is updated or if an error occurs.
    
    Raises:
    - Http404: If no post or comment matching the provided slug and ID is found.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# This view handles comment deleting functionality.
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

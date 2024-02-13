from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Renders a detailed view of a blog post identified by a slug.
    This view retrieves and displays
    the details of a specific `Post` object, including its comments.
    It supports displaying commentsin descending order based on their creation
     time and allows authenticated users to submit new comments
    on the post.

    The view filters `Post` objects to include only those with a status of 1
    (typically meaning 'published').
    It raises a 404 error if no post matches the given slug.
    For authenticated users submitting a comment,
    the view processes the comment form on POST requests,
    creates a new comment associated with the post,
    and saves it to the database.
    A success message is displayed upon the successful submission of a comment.

    **Context**

    - `post`: The `Post` instance being viewed. This includes all the data
    associated with the post.
    - `comments`: A queryset of `Comment` instances associated with the post,
    ordered from newest to oldest.
    - `comment_count`: The total number of approved comments for the post.
    - `comment_form`: An instance of `CommentForm` to be displayed in the
    template for submitting new comments.

    **Template**

    - `blog/post_detail.html`: The template used to render the post details,
    including its comments and the comment submission form.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - slug (str): The slug of the `Post` to be displayed. Used to uniquely
    identify the post.

    Returns:
    - HttpResponse: Renders the `blog/post_detail.html` template with the post
    details, comments, and comment form context.
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment submitted')
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
    })

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

    This view function allows users to edit their comments on a blog post.
    It first checks if the request is a POST.
    If so, it attempts to fetch the specific post and comment using
    the provided `slug` and `comment_id`.
    It then creates a `CommentForm` instance with the POST data and the comment
    instance to be edited.
    If the form is valid and the user making the request is the author of the
    comment, it updates the comment,
    marks it as not approved, and saves it. A success message is added to the
    messages framework.
    If there are any errors, an error message is added instead.

    Parameters:
    - request (HttpRequest): The HTTP request sent to the view, containing
    method and POST data.
    - slug (str): The slug of the post to which the comment belongs. Used to
    identify the specific post.
    - comment_id (int): The ID of the comment to be edited. Used to identify
    the specific comment.

    Returns:
    - HttpResponseRedirect: Redirects to the detail page of the post after the
    comment is updated or if an error occurs.

    Raises:
    - Http404: No matching post/comment for slug/ID.
    """
    if request.method == "POST":

        queryset = Post.objects.all()
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
    Handles the deletion of a user's comment on a specific post.

    This view function is responsible for allowing users to delete their own
    comments from a blog post. It does so by first
    retrieving the post using the given `slug` and ensuring the post exists and
    is published (status=1). It then attempts
    to fetch the comment to be deleted using the provided `comment_id`. If the
    user making the request is the author of
    the comment, the comment is deleted, and a success message is displayed. If
    the user is not the author, an error
    message is shown, indicating that users can only delete their own comments.

    Parameters:
    - request (HttpRequest): The HTTP request sent to the view. This includes
    the user making the request.
    - slug (str): The slug of the post from which the comment is to be deleted.
    Used to identify the specific post.
    - comment_id (int): The ID of the comment to be deleted. Used to identify
    the specific comment.

    Returns:
    - HttpResponseRedirect: Redirects to the detail page of the post after the
    comment is deleted or if an error occurs.

    Notes:
    - The view relies on the user being authenticated and matching the author
    of the comment for deletion to proceed.
    - Uses Django's messaging framework to provide feedback to the user about
    the action's success or failure.
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

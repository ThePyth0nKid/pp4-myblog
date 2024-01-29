from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
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
    comment_count = post.comments.filter(approved=True).count()

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
                'Comment submitted and awaiting approval'
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

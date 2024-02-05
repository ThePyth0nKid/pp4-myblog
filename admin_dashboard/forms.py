from django import forms
from django_summernote.widgets import SummernoteWidget
from blog.models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions


class PostForm(forms.ModelForm):
    """
    A form for creating and editing blog posts, excluding the 'author' field
    as it is intended to be automatically set to the current user in the view.

    Attributes:
        title (str): The title of the blog post.
        slug (str): The URL-friendly slug for the blog post.
        featured_image (ImageField): An optional featured image for the blog post.
        content (TextField): The main content of the blog post, using Django Summernote for rich text editing.
        status (ChoiceField): The status of the blog post (e.g., draft, published).
        excerpt (CharField): A brief excerpt or summary of the blog post.
        updated_on (DateTimeField): The date and time when the blog post was last updated.

    Methods:
        __init__(self, *args, **kwargs): Constructor method for initializing the form.
    """

    class Meta:
        model = Post
        fields = ['title', 'slug', 'featured_image',
                  'content', 'status', 'excerpt', 'updated_on']
        widgets = {
            # Apply Django Summernote to the 'content' field for rich text editing.
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        """
        Constructor method for initializing the PostForm.

        Parameters:
            *args: Positional arguments to pass to the parent class constructor.
            **kwargs: Keyword arguments to pass to the parent class constructor.
        """
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'

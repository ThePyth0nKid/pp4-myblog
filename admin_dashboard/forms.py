from django import forms
from blog.models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions


class PostForm(forms.ModelForm):
    """
    A form for creating and editing blog posts, excluding the 'author' field
    as it is intended to be automatically set to the current user in the view.
    """
    class Meta:
        model = Post
        fields = ['title', 'slug', 'featured_image',
                  'content', 'status', 'excerpt', 'updated_on']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'

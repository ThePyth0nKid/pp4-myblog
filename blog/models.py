from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True)  # Added SlugField
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        if not self.slug:  # Check if slug is not provided
            self.slug = slugify(self.title)  # Generate slug from title
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

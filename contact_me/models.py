from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Initial slug creation from subject
            original_slug = slugify(self.subject)
            unique_slug = original_slug
            counter = 1
            while Contact.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{original_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Message from {self.name}"

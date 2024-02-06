from django.db import models
from django.utils.text import slugify
# Importieren Sie timezone für das created_at-Feld
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    # Hinzugefügtes created_at-Feld
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject)
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return f"Message from {self.name}"

        return f"Message from {self.name}"

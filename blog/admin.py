from django.contrib import admin
from .models import Post, Comment

# Register the Post model with Django admin using the default ModelAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'slug')
    # Allow searching by title and content
    search_fields = ['title', 'content']
    # Enable filtering by the created_on field
    list_filter = ('created_on',)
    # Automatically populate the slug field from the title
    prepopulated_fields = {'slug': ('title',)}
    # Specify which fields should use the default text editor.
    # If using Summernote or another rich text editor, you'd configure it here.
    # Since we're using the default ModelAdmin, this configuration is for standard Django fields.


# Register the Comment model with Django admin using the default registration method
# This allows managing comments in the admin interface without custom configurations.
admin.site.register(Comment)

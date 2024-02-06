from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    # Add the new fields to be displayed in the admin list
    list_display = ('name', 'email', 'subject', 'created_at')
    # Automatically populate the Slug field based on the Subject field
    prepopulated_fields = {'slug': ('subject',)}


admin.site.register(Contact, ContactAdmin)

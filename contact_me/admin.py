from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    summernote_fields = ('message',)
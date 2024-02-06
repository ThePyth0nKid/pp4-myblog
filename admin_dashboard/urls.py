from django.urls import path
from .views import admin_messages, create_post, delete_post, delete_contact


urlpatterns = [
    path('', admin_messages, name='admin_dashboard'),
    path('create/', create_post, name='create_post'),
    path('delete_contact/<slug:slug>/', delete_contact, name='delete_contact'),
]

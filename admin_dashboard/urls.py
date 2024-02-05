from django.urls import path
from .views import admin_messages, create_post, delete_post


urlpatterns = [
    path('', admin_messages, name='admin_dashboard'),
    path('create/', create_post, name='create_post'),
    path('create_post/<int:post_id>/', create_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]

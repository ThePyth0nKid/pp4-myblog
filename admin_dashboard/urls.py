from django.urls import path
from .views import admin_messages, create_post


urlpatterns = [
    path('', admin_messages, name='admin_dashboard'),
    path('create/', create_post, name='create_post')
]

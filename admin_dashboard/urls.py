from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin_messages, name='admin_dashboard'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.create_new_user, name = 'create_user'),
]

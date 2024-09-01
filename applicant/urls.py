from django.urls import path
from . import views

urlpatterns = [
    # Example path, replace 'create_resume' and 'views.create_resume' with your actual view and path names
    path('create/', views.create_resume, name='create_resume'),
]
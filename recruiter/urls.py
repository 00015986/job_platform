# from django.urls import path
# from . import views
# from django.views.generic import TemplateView
#
# urlpatterns = [
#     path('myapp/list/', views.ProductListView.as_view(), name='product_list'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    # Example path, replace 'create_job' and 'views.create_job' with your actual view and path names
    path('recruiter/create/', views.create_job, name='create_job'),
]

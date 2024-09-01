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
    # Define your admin panel-related URLs here
    # Example:
    path('adminpanel/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # Add more paths as needed
]

from django.urls import path
from . import views

urlpatterns = [
    path('home_platform/list/', views.JobListView.as_view(), name='job_list'),
    path('home_platform/allJobs/', views.AllJobsListView.as_view(), name='all_jobs'),
    path('accounts/signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('home_platform/recruiter_dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('home_platform/applicant_dashboard/', views.applicant_dashboard, name='applicant_dashboard'),
]



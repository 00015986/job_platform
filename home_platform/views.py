from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from recruiter.models import Job
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import CustomSignupForm
from django.contrib.auth.decorators import login_required

from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from allauth.account.views import SignupView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy


# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    context = {
        "jobs": jobs
    }
    return render(request, 'homePage_list.html', context)


class JobListView(ListView):
    model = Job
    template_name = "homePage_list.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return self.model.objects.order_by("id")


class AllJobsListView(ListView):
    model = Job
    template_name = "all_jobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return self.model.objects.order_by("id")

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def get_success_url(self):
        if self.request.user.is_applicant():
            return reverse('applicant_dashboard')
        elif self.request.user.is_recruiter():
            return reverse('recruiter_dashboard')
        elif self.request.user.is_admin():
            return reverse('admin_dashboard')
        elif self.request.user.is_moderator():
            return reverse('moderator_dashboard')
        return super().get_success_url()


@login_required
def recruiter_dashboard(request):
    # Add any context data needed for the recruiter dashboard
    context = {
        'title': 'Recruiter Dashboard',
        # Add more context as needed
    }
    return render(request, 'recruiter/homePage_list_recruiter.html', context)

@login_required
def applicant_dashboard(request):
    # Add any context data needed for the applicant dashboard
    context = {
        'title': 'Applicant Dashboard',
        # Add more context as needed
    }
    return render(request, 'applicant/homePage_list_applicant.html', context)

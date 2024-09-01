from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .form import JobForm

# Create your views here.
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'recruiter/create_job.html', {'form': form})


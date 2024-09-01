from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm

# Create your views here.
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_list')  # Redirect to a view that lists resumes or a success page
    else:
        form = ResumeForm()
    return render(request, 'applicant/create_resume.html', {'form': form})




from django.db import models
from django.conf import settings
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='Unknown')
    recruiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    founded_year = models.IntegerField(default=2003)
    # job = models.ForeignKey("Job", on_delete=models.CASCADE)
    # Other fields

class Job(models.Model):
    JOB_TYPES = (
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('0T', 'Onsite'),
        ('RT', 'Remote'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    industry = models.CharField(max_length=255, default='Technology')
    job_type = models.CharField(max_length=2, choices=JOB_TYPES, default='FT')
    location = models.CharField(max_length=255, default='Unknown')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_filled = models.BooleanField(default=False)
    posted_date = models.DateTimeField(default=timezone.now)

    def get_time_since_posted(self):
        now = timezone.now()
        delta = now - self.posted_date
        if delta.days > 0:
            return f'{delta.days} days ago'
        hours = delta.seconds // 3600
        if hours > 0:
            return f'{hours} hours ago'
        minutes = (delta.seconds % 3600) // 60
        return f'{minutes} minutes ago'


class ApplyJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applied_jobs")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applied_users")

class HiredUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="hired_user")
    recruiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="hired_recruiter")
    created_at = models.DateTimeField(auto_now_add=True)
"""
One to Many
Company 1 -> Job 1, Job 2, Job 3



Many to One
Company 1, Company 2, Company 3 -> Job 1 


Many to Many
Google -> Recruiter 1
Amazon -> Recruiter 1
Google -> Recruiter 2
Amazon -> Recruiter 2

One to One
Company 1 - Job 1

"""
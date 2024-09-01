from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('applicant', 'Applicant'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='applicant')

    def is_applicant(self):
        return self.role == 'applicant'

    def is_recruiter(self):
        return self.role == 'recruiter'

    def is_admin(self):
        return self.role == 'admin'

    def is_moderator(self):
        return self.role == 'moderator'

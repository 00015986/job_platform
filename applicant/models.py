from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


# Create your models here.

class Resume(models.Model):
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # other fields...

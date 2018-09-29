from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from ..loginreg.models import *
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your models here.


# @method_decorator(login_required, name='dispatch')
# class ProtectedView(TemplateView):
#     template_name = 'main/home.html'


class JobManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['titlethere'] = "Title must not be blank."
        if len(postData['title']) < 4:
            errors['titlelength'] = "Title must be at least 4 characters."
        if len(postData['description']) < 1:
            errors['descriptionthere'] = "Description must not be blank."
        if len(postData['description']) < 11:
            errors['descriptionlength'] = "Description must be at least 11 characters."
        if len(postData['location']) < 1:
            errors['locationlength'] = "Location must not be blank."
        return errors

class Job(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    location = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user_created = models.ForeignKey(User, related_name = "job_created", on_delete='models.CASCADE')
    user_taking = models.ManyToManyField(User, related_name = "job_user_taking")
    objects = JobManager()
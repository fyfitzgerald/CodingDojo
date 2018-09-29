from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['f_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if not postData['f_name'].isalpha():
            errors["first_name_alpha"] = "First name should be only letters"
        if len(postData['l_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if not postData['l_name'].isalpha():
            errors["last_name_alpha"] = "Last name should be only letters"
        if len(postData['email_address']) < 1:
            errors["email"] = "Email cannot be blank!"
        elif not EMAIL_REGEX.match(postData['email_address']):
            errors["email_invalid"] = "Invalid Email Address!"
        potential_matches = User.objects.filter(email = postData['email_address'])
        if len(potential_matches) > 0:
            errors["email_uniqueness"] = "Email already exists"
        if len(postData['pword']) < 8:
            errors["pword"] = "Password should be at least 8 charactes"
        if postData['pword'] != postData['conf_pword']:
            errors['conf_pword'] = "Passwords must match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {}>".format(self.first_name)
# Create your models here.

from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from ..loginreg.models import *
from datetime import datetime
from django.contrib.auth.decorators import login_required


class QuoteManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['author']) < 1:
            errors['authorthere'] = "Author must not be blank."
        if len(postData['author']) < 4:
            errors['authorlength'] = "Author must be at least 4 characters."
        if len(postData['quote']) < 1:
            errors['quotethere'] = "Quote must not be blank."
        if len(postData['quote']) < 11:
            errors['quotelength'] = "Quote must be at least 11 characters."
        return errors

class Quote(models.Model):
    content = models.TextField()
    author = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user_created = models.ForeignKey(User, related_name = "quote_created", on_delete='models.CASCADE')
    user_liking = models.ManyToManyField(User, related_name = "quote_user_liking")
    objects = QuoteManager()
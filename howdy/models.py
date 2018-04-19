from __future__ import unicode_literals

from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    long_description = models.CharField(max_length=2000)
    short_description = models.CharField(max_length=1000)
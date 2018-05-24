from __future__ import unicode_literals

from django.db import models

class Company(models.Model):
    name =      models.CharField(max_length=250)
    logo_url =  models.CharField(max_length=500)

class Job(models.Model):
    company =           models.ForeignKey(Company, on_delete=models.CASCADE)
    city =              models.CharField(max_length=250)
    state =             models.CharField(max_length=250)
    title =             models.CharField(max_length=500)
    description =       models.CharField(max_length=2000)
    link =              models.CharField(max_length=500)
    date_added =        models.DateTimeField(auto_now_add=True)

    class Meta:
        # sort by date in descending order unless
        # overridden in the query with order_by()
        ordering = ['-date_added']
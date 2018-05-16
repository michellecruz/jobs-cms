from __future__ import unicode_literals

from django.db import models

class Company(models.Model):
    company_name =      models.CharField(max_length=250)
    company_logo_url =  models.CharField(max_length=250)

class Job(models.Model):
    company =           models.ForeignKey(Company, on_delete=models.CASCADE)
    city =              models.CharField(max_length=250)
    state =             models.CharField(max_length=250)
    job_title =         models.CharField(max_length=500)

    JUNIOR = 'JR'
    MIDLEVEL = 'MID'
    SENIOR = 'SR'
    INTERN = 'INTERN'
    joblevel = (
        (JUNIOR, 'Junior Staff'),
        (MIDLEVEL, 'Midlevel Staff'),
        (SENIOR, 'Senior Staff'),
        (INTERN, 'Internship')
    )

    job_level =         models.CharField(
                            max_length=100,
                            choices=joblevel,
                            default=MIDLEVEL
                        )
    description =       models.CharField(max_length=2000)
    created_at =        models.DateTimeField(auto_now_add=True)
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from models import Company, Job


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        return context


class JobDetails(TemplateView):
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        job_id = self.request.path.split('/')
        job_id = job_id[-1]

        context = super(JobDetails, self).get_context_data(**kwargs)
        context['job'] = Job.objects.get(id=job_id)
        return context
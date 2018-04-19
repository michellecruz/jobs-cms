from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from models import Company, Job

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
       context = super(HomePageView, self).get_context_data(**kwargs)
       context['jobs'] = Job.objects.all()
       return context


class AddJobView(TemplateView):
    template_name = 'admin/create.html'


class AddJobHandler(TemplateView):
    template_name = 'admin/create.html'

    def post(self, request, **kwargs):
        # Company Info
        company_name = request.POST.get('company_name')
        location_city = request.POST.get('location_city')
        location_state = request.POST.get('location_state')

        # Job Info
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        short_job_description = request.POST.get('short_job_description')


        company_validation = Company.objects.filter(company_name=company_name)

        if company_validation.count() == 0:
            try:
                c = Company.objects.create(
                        company_name=company_name,
                        city=location_city,
                        state=location_state
                    )
                c.save()

                c = Company.objects.get(pk=c.pk)
                j = Job.objects.create(
                        company=c,
                        title=job_title,
                        long_description=job_description,
                        short_description=short_job_description
                    )
                j.save()

                return redirect('/')
            except:
                return redirect('/create')
        else:
            try:
                company_validation_id = company_validation.values_list('id', flat=True)
                c = Company.objects.get(pk=company_validation_id)
                j = Job.objects.create(
                        company=c,
                        title=job_title,
                        long_description=job_description,
                        short_description=short_job_description
                    )
                j.save()

                return redirect('/')
            except:
                return redirect('/create')

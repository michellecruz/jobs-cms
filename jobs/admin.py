from django.conf.urls import url
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from models import Company, Job

from django.contrib import admin
from django.contrib.auth.models import User


# PAGE: Main Admin Panel (/admin)
class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/login/'
    template_name = 'admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        return context


# PAGE: Settings (/admin/settings)
class SettingsView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/login'
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)
        context['admin_users'] = User.objects.all().order_by('username')
        return context


# HANDLER: Add User (/admin/settings)
class AddUserHandler(LoginRequiredMixin, View):
    login_url = '/admin/login'
    redirect_field_name = '/settings'

    def post(self, request, **kwargs):
        # User info
        username = request.POST.get('username')
        password = request.POST.get('password')

        username_validation = User.objects.filter(username=username)


        if username_validation.count() == 0:
        # If username is not taken, add user to the database.
            try:
                user = User.objects.create_user(username=username,
                                                password=password)
                return redirect('/admin/settings')
            except:
                return redirect('/admin/settings')
        else:
            return redirect('/admin/settings')


# HANDLER: Delete User (/admin/settings)
class DeleteUserHandler(LoginRequiredMixin, View):
    login_url = '/admin/login'
    redirect_field_name = '/admin/settings'

    def post(self, request, **kwargs):
        user_id = request.POST.get('user_id')
        u = User.objects.get(pk=user_id)

        try:
        # Deletes user from database.
            u.delete()

            return redirect('/admin/settings')
        except:
            return redirect('/admin/settings')


# PAGE: Add Job (/admin/create)
class AddJobView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/login'
    template_name = 'admin/create.html'


# HANDLER: Add or Edit Job (/admin/create or /admin/edit/..)
class AddEditJobHandler(LoginRequiredMixin, TemplateView):
    login_url = '/admin/login'
    template_name = 'admin/create.html'

    def get_context_data(self, **kwargs):
        context = super(AddEditJobHandler, self).get_context_data(**kwargs)
        current_path = self.request.path.split('/')

        if current_path[-2] == 'edit':
            context['edit_mode'] = True
            job_id = current_path[-1]
            context['job'] = Job.objects.get(pk=job_id)
        else:
            context['edit_mode'] = False

        return context

    def post(self, request, **kwargs):
        # If in edit mode, this returns the job ID
        # otherwise it returns None.
        job_id = request.POST.get('job_id')
        is_new_entry = True if job_id is None else False

        # Company Info
        company_name =      request.POST.get('company_name')
        company_logo_url =  request.POST.get('company_logo_url')

        # Job Info
        location_city =     request.POST.get('location_city')
        location_state =    request.POST.get('location_state')
        job_title =         request.POST.get('job_title')
        job_description =   request.POST.get('job_description')
        job_link =          request.POST.get('job_link')

        company_validation = Company.objects.filter(name=company_name)

        if is_new_entry:
            if company_validation.count() == 0:
            # If company name is not in the database, add company
            # and job to the database.
                try:
                    c = Company.objects.create(
                            name=company_name,
                            logo_url=company_logo_url
                        )
                    c.save()

                    c = Company.objects.get(pk=c.pk)
                    j = Job.objects.create(
                            company=c,
                            city=location_city,
                            state=location_state,
                            title=job_title,
                            description=job_description,
                            link=job_link
                        )
                    j.save()

                    return redirect('/admin')
                except:
                    return redirect('/admin/create')
            else:
            # If company name is in the database, add job to the database
            # and connect it to existing company.
                try:
                    company_validation_id = company_validation.values_list('id', flat=True)

                    c = Company.objects.get(pk=company_validation_id)
                    j = Job.objects.create(
                            company=c,
                            city=location_city,
                            state=location_state,
                            title=job_title,
                            description=job_description,
                            link=job_link
                        )
                    j.save()

                    return redirect('/admin')
                except:
                    return redirect('/admin/create')
        else:
            try:
                j = Job.objects.get(pk=job_id)
                j.city =        location_city
                j.state =       location_state
                j.title =       job_title
                j.description = job_description
                j.link =        job_link
                j.save()

                return redirect('/admin')
            except:
                return redirect('/admin')


# HANDLER: Delete Job (/admin)
class DeleteJobHandler(LoginRequiredMixin, View):
    login_url = '/admin/login'
    redirect_field_name = '/admin'

    def post(self, request, **kwargs):
        job_id = request.POST.get('job_id')
        j = Job.objects.get(pk=job_id)

        # Counts how many jobs this company has in the database.
        jobs_count = Job.objects.filter(company=j.company).count()

        if jobs_count == 1:
        # If company is only linked to one job, delete
        # both job and company from the database.
            try:
                j.company.delete()

                return redirect('/admin')
            except:
                return redirect('/admin')
        else:
            try:
            # Deletes job from database.
                j.delete()

                return redirect('/admin')
            except:
                return redirect('/admin')





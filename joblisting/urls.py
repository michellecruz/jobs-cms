"""joblisting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include

from jobs import admin as admin_view

urlpatterns = [
    # Views
    url(r'^', include('jobs.urls')),

    # Admin Views
    url(r'^admin/',                 include('django.contrib.auth.urls')),
    url(r'^admin/settings',         admin_view.SettingsView.as_view(),      name='settings'),
    url(r'^admin/create',           admin_view.AddJobView.as_view(),        name='create'),
    url(r'^admin/edit/([\w\-]+)',   admin_view.AddEditJobHandler.as_view(), name='edit'),

    # Admin Handlers
    url(r'^admin/add_user',         admin_view.AddUserHandler.as_view(),    name='add_user'),
    url(r'^admin/delete_user',      admin_view.DeleteUserHandler.as_view(), name='delete_user'),
    url(r'^admin/post',             admin_view.AddEditJobHandler.as_view(), name='post'),
    url(r'^admin/delete',           admin_view.DeleteJobHandler.as_view(),  name='delete'),

    # Admin Dashboard
    # ORDER MATTERS. Put this last so that the app
    # goes through the views above first.
    url(r'^admin/',                 admin_view.DashboardView.as_view(),     name='admin'),
]
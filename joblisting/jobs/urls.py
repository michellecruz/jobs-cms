from django.conf.urls import url
from jobs import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^details$', views.JobDetails.as_view(), name='details'),
    url(r'^create$', views.AddJobView.as_view(), name='create'),
    url(r'^post$', views.AddJobHandler.as_view(), name='job_save'),
]
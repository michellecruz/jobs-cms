from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'create', views.AddJobView.as_view()),
    url(r'post', views.AddJobHandler, name='job_save')
]

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^create$', views.AddJobView.as_view(), name='create'),
    url(r'^post$', views.AddJobHandler.as_view(), name='job_save'),
]
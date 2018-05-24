from django.conf.urls import url
from jobs import views

urlpatterns = [
    # Views
    url(r'^$',                      views.HomePageView.as_view(),   name='index'),
    url(r'^details/([\w\-]+)/?$',   views.JobDetails.as_view(),     name='details'),
]
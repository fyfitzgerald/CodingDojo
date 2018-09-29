from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^main$', views.main),
    url(r'^addajob$', views.add_a_job),
    url(r'^process_job_add$', views.process_job_add),
    url(r'^view_job/(?P<number>\d+)$', views.view_job),
    url(r'^edit_job/(?P<number>\d+)$', views.edit_job),
    url(r'^process_job_update/(?P<id>\d+)$', views.process_job_update),
    url(r'^delete_job/(?P<number>\d+)$', views.delete_job),
    url(r'^logout$', views.logout),
]
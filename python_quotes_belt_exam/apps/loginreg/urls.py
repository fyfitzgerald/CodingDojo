from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^validate_login$', views.validate_login),
    # url(r'^success$', views.success),
]
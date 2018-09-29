from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^validate_login$', views.validate_login),
    url(r'^success$', views.success),
    url(r'^post_message$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^delete_message$', views.delete_message),
    url(r'^delete_comment$', views.delete_comment),
]
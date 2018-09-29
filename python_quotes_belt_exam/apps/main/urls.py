from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^main$', views.main),
    url(r'^process_quote_add$', views.process_quote_add),
    url(r'^view_user_quotes/(?P<id>\d+)$', views.view_user_quotes),
    url(r'^edit_user_account/(?P<id>\d+)$', views.edit_user_account),
    url(r'^process_acct_update/(?P<id>\d+)$', views.process_acct_update),
    url(r'^delete_quote/(?P<id>\d+)$', views.delete_quote),
    url(r'^logout$', views.logout),
]
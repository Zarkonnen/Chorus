from django.conf.urls import include, url
from chorusp.chorus.views import home, live

urlpatterns = [
    url(r'^/?$', home, name='home'),
    url(r'^live/?$', live, name='live')
]

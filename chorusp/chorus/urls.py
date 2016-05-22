from django.conf.urls import include, url
from chorusp.chorus.views import home, chores, live

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^([a-zA-Z0-9_]+)/?$', chores, name='chores'),
    url(r'^([a-zA-Z0-9_]+)/live/?$', live, name='live')
]

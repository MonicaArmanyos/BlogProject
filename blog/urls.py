from django.conf.urls import include, url
from blog import views

urlpatterns = [
    url(r'^homepage/$', views.homepage),
    url(r'^register$', views.register),
    url(r'^logout$', views.user_logout),
    url(r'^user_login$', views.user_login),
    url(r'^special$', views.special),
    url(r'^search/$', views.search),
]

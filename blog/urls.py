from django.conf.urls import include, url
from . import views
from blog import views

urlpatterns = [
    url(r'^homepage/$', views.homepage,name='index'),
    url(r'^register$', views.register),
    url(r'^logout$', views.user_logout),
    url(r'^login$', views.user_login),
    url(r'^special$', views.special),
    url(r'^postdetails/(?P<post_id>[0-9]+)$', views.getProduct),
    url(r'^like/(?P<post_id>[0-9]+)$', views.makelike),

]

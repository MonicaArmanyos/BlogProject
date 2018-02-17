from django.conf.urls import include, url
from blog import views

urlpatterns = [

    url(r'^homepage/$', views.homepage),
    url(r'^register$', views.register),
    url(r'^logout$', views.user_logout),
    url(r'^login$', views.user_login),
    url(r'^special$', views.special),
    url(r'^search/$', views.search),
    url(r'^homepage/(?P<cat_id>[0-9]+$)', views.getCategoryPosts),
    url(r'^homepage/sub/(?P<cat_id>[0-9]+)/(?P<user_id>[0-9]+$)', views.subscribe),
    url(r'^homepage/unsub/(?P<cat_id>[0-9]+)/(?P<user_id>[0-9]+$)', views.unsubscribe),
]

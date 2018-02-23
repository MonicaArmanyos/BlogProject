from django.conf.urls import include, url
from blog import views

urlpatterns = [

    url(r'^homepage/$', views.homepage, name='index'),
    url(r'^register$', views.register),
    url(r'^logout$', views.user_logout),
    url(r'^login$', views.user_login),
    url(r'^special$', views.special),
    url(r'^homepage/search/$', views.search),
    url(r'^homepage/(?P<cat_id>[0-9]+$)', views.getCategoryPosts),
    url(r'^sub/$', views.subscribe),
    url(r'^unsub/$', views.unsubscribe),
    url(r'^post/(?P<post_id>[0-9]+)$', views.post),
    url(r'^comment/$', views.comment),
    url(r'^reply/$', views.reply),
    url(r'^like/(?P<post_id>[0-9]+)$', views.makelike),
    url(r'^dislike/(?P<post_id>[0-9]+)$', views.makedislike),
    url(r'^postNotFound', views.postNotFound),
]

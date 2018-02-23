from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^dashboard$', views.dashBoard),
    url(r'^allPosts/$', views.allPosts),
    url(r'^addPost/$', views.addPost),
    url(r'^editPost/(?P<post_id>[0-9]+)/$', views.editPost),
    url(r'^deletePost/(?P<post_id>[0-9]+)/$', views.deletePost),
    url(r'^allCategories/$', views.allCategories),
    url(r'^addCategory/$', views.addCategory),
    url(r'^editCategory/(?P<category_id>[0-9]+)/$', views.editCategory),
    url(r'^deleteCategory/(?P<category_id>[0-9]+)/$', views.deleteCategory),
    url(r'^allWords/$', views.allWords),
    url(r'^addWord/$', views.addWord),
    url(r'^editWord/(?P<word_id>[0-9]+)/$', views.editWord),
    url(r'^deleteWord/(?P<word_id>[0-9]+)/$', views.deleteWord),
    url(r'^allTags/$', views.allTags),
    url(r'^addTag/$', views.addTag),
    url(r'^addUser/$', views.addUser),
    url(r'^editTag/(?P<tag_id>[0-9]+)/$', views.editTag),
    url(r'^deleteTag/(?P<tag_id>[0-9]+)/$', views.deleteTag),
    url(r'^allUsers/$', views.allUsers),
    url(r'^blockUser/(?P<user_id>[0-9]+)/$', views.blockUser),
    url(r'^unblockUser/(?P<user_id>[0-9]+)/$', views.unblockUser),
    url(r'^promoteUser/(?P<user_id>[0-9]+)/$', views.promoteUser),
    url(r'^editUser/(?P<user_id>[0-9]+)/$', views.editUser),
    url(r'^deleteUser/(?P<user_id>[0-9]+)/$', views.deleteUser),

    
]

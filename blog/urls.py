from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^about$', views.AboutView.as_view(), name='about'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit$', views.UpdatePostView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete$', views.DeletePostView.as_view(), name='post_delete'),
    url(r'^draft$', views.DraftListView.as_view(), name='post_draft'),
    url(r'^post/(?P<pk>\d+)/publish$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove$', views.comment_delete, name='comment_delete'),
]

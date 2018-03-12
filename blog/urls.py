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
]

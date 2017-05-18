from django.conf.urls import url
from neulyferreira.frontend import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^posts/', views.posts, name='posts'),
    url(r'^post_detail/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail')
]

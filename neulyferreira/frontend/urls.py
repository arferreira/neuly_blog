from django.conf.urls import url
from neulyferreira.frontend import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

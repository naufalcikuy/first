from django.conf.urls import url
from . import views
from . import admin



urlpatterns = [
    url(r'^history/$', views.new_history, name='new_history'),
    url(r'^$', views.knowledge_list, name='knowledge_list'),
    url(r'^knowledge/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^knowledge/new/$', views.post_new, name='post_new'),
    url(r'^knowledge/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^show/knowledge$', views.show_knowledge, name='show_knowledge'),
    url(r'^show/history$', views.show_history, name='show_history'),
    url(r'^show/event$', views.show_event, name='show_event'),

]
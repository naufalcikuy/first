from django.conf.urls import url
from . import views
from . import admin



urlpatterns = [
    url(r'^history/$', views.new_history, name='new_history'),
    url(r'^$', views.knowledge_list, name='knowledge_list'),
    url(r'^knowledge/(?P<id_knowledge>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^knowledge/new/$', views.post_new, name='post_new'),
    url(r'^knowledge/(?P<id_knowledge>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^show/knowledge$', views.show_knowledge, name='show_knowledge'),
    url(r'^show/history$', views.show_history, name='show_history'),
    url(r'^show/event$', views.show_event, name='show_event'),
    url(r'^manage/knowledge$', views.show_pengetahuan, name='show_pengetahuan'),
   # url(r'^manage/knowledge/edit$', views.new_knowledge, name='new_knowledge'),
    url(r'^manage/knowledge/edit/(?P<id_knowledge>[0-9]+)/$', views.edit_knowledge, name='edit_knowledge'),
    url(r'^manage/knowledge/delete/(?P<id_knowledge>[0-9]+)/$', views.delete_knowledge, name='delete_knowledge'),
    url(r'^manage/knowledge/(?P<id_knowledge>[0-9]+)/$', views.detail_knowledge, name='detail_knowledge'),

    url(r'^manage/member$', views.show_anggota, name='show_anggota'),
    url(r'^manage/member/edit/(?P<id_bayi>[0-9]+)/$', views.edit_member, name='edit_member'),
    url(r'^manage/member/(?P<id_bayi>[0-9]+)/$', views.detail_member, name='detail_member'),
    url(r'^manage/member/delete/(?P<id_bayi>[0-9]+)/$', views.delete_member, name='delete_member'),
    url(r'^manage/member/new$', views.new_member, name='new_member'),
    url(r'^manage/check$', views.show_pemeriksaan, name='show_pemeriksaan'),
    url(r'^manage/event$', views.show_kegiatan, name='show_kegiatan'),
    url(r'^manage/event/new$', views.new_event, name='new_event'),
    url(r'^manage/event/edit/(?P<id_event>[0-9]+)/$', views.edit_event, name='edit_event'),
    url(r'^manage/event/(?P<id_event>[0-9]+)/$', views.detail_event, name='detail_event'),
    url(r'^manage/event/delete/(?P<id_event>[0-9]+)/$', views.delete_event, name='delete_event'),

 
    ] 
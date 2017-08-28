from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /new/
    url(r'^new/$', views.new_post, name='new'),
    # ex: /1/view/
    url(r'^(?P<post_id>[0-9]+)/$', views.view_post, name='view_post'),
    # ex: /archive/2017/
    url(r'^archive/(?P<year_var>[0-9]+)/$', views.year_archive, \
        name='year_archive'),
    # ex: /archive/2017/6/
    url(r'^archive/(?P<year_var>[0-9]+)/(?P<month_var>[0-9]+)/$', \
        views.month_archive, name='month_archive'),
    # ex: /archive/2017/6/28
    url(r'^archive/(?P<year_var>[0-9]+)/(?P<month_var>[0-9]+)/(?P<day_var>[0-9]+)/$', views.day_archive, name='day_archive'),
    # ex: /register/
    url(r'^register/$', views.guest_register, name='register'),
    # ex: /login/
    url(r'^login/$', views.guest_login, name='login'),
    # ex: /logout/
    url(r'^logout/$', views.guest_logout, name='logout'),
    # ex: /1/comment/
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment_post, name='comment'),
    # ex: /1/comment/delete/
    url(r'^(?P<post_id>[0-9]+)/comment/(?P<comment_id>[0-9]+)/$', \
        views.comment_delete, name='comment_delete'),
    # ex: /1/delete/
    url(r'^(?P<post_id>[0-9]+)/delete/$', views.delete_post, name='delete'),
    # ex: /1/edit/
    url(r'^(?P<post_id>[0-9]+)/edit/$', views.edit_post, name='edit'),
    # ex: /1/like/
    url(r'^(?P<post_id>[0-9]+)/like/$', views.like_post, name='like'),
]

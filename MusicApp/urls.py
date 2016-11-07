from django.conf.urls import url
from . import views

app_name ='MusicApp'

urlpatterns = [
    # /music/
    url(r'^$',views.index,name="index"),
    # /login/
    url(r'^login/$',views.LoginFormView.as_view(),name="login"),
    # /logout/
    url(r'^logout/$',views.logout_user,name="logout"),
    #/register/
    url(r'^register/$',views.UserFormView.as_view(),name="register"),
    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    # /music/album/add/
    url(r'^album/add$', views.AlbumCreate.as_view(), name='album_add'),
    # /music/song/add
    url(r'^song/add/$', views.SongCreate.as_view(), name='song_add'),
    # /music/album/<pk>/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album_update'),
    # /music/album/<pk>/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album_delete'),



]
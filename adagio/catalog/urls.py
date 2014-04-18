from django.conf.urls import patterns, url
from . import api

urlpatterns = patterns(
    'catalog.api',

    url(r'^artists/$',
        api.ArtistList.as_view(),
        name='artist-list'),

    url(r'^artists/(?P<pk>[0-9]+)/$',
        api.ArtistDetail.as_view(),
        name='artist-detail'),

    url(r'^albums/$',
        api.AlbumList.as_view(),
        name='album-list'),

    url(r'^albums/(?P<pk>[0-9]+)/$',
        api.AlbumDetail.as_view(),
        name='album-detail'),

    url(r'^tracks/$',
        api.TrackList.as_view(),
        name='track-list'),

    url(r'^tracks/(?P<pk>[0-9]+)/$',
        api.TrackDetail.as_view(),
        name='track-detail'),

    url(r'^import/$',
        api.CatalogImport.as_view(),
        name='catalog-import'),
)

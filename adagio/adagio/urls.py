from collections import OrderedDict
from django.conf.urls import patterns, include, url
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

##
# Set up our API root
##


@api_view(['GET'])
def adagio_api_root(request, format=None):
    '''
    Below are the main entry points to the Adagio API.
    Each API will provide additional endpoints to step
    through to any underlying resources.
    '''

    # Use OrderedDict to keep the insertion order in
    # the return JSON
    api = OrderedDict()
    api['artists'] = reverse('artist-list',
                             request=request,
                             format=format)
    api['albums'] = reverse('album-list',
                            request=request,
                            format=format)
    api['tracks'] = reverse('track-list',
                            request=request,
                            format=format)
    api['import'] = reverse('catalog-import',
                            request=request,
                            format=format)
    api['docs'] = reverse('django.swagger.base.view',
                          request=request,
                          format=format)
    return Response(api)

# Set our urlpatterns that Django requires
urlpatterns = patterns(
    '',

    # Show are API root for browsing - as defined above.
    url(r'^$', adagio_api_root),

    # Bring in the various API endpoints from the catalog app
    url(r'^', include('catalog.urls')),

    # Also enable swagger
    url(r'^docs/', include('rest_framework_swagger.urls')),
)

# Uncomment the block below to see how we can use
# rest_framework routers to simplify the API endpoint
# creation. There are tradeoffs with this approach,
# but easily handled by subclassing one of the routers
# to achieve what you're after.
'''
from catalog import viewsets, api

router = DefaultRouter()
router.register(r'artists', viewsets.ArtistViewSet)
router.register(r'albums', viewsets.AlbumViewSet)
router.register(r'tracks', viewsets.TrackViewSet)

# Set our urlpatterns that Django requires
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
'''

# When in debug mode, it's usually beneficial to enable the wonderful
# django debug toolbar for profiling various things. In particular, its
# SQL profiling panel is amazingly useful.
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),

    )

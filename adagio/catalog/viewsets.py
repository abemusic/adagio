from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from . import models, serializers


class ArtistViewSet(ModelViewSet):
    '''
    All CRUD APIs available for manipulating Artist model objects.
    '''

    model = models.Artist
    serializer_class = serializers.ArtistSerializer
    parser_classes = (JSONParser,)


class AlbumViewSet(ModelViewSet):
    '''
    All CRUD APIs available for manipulating Album model objects.
    '''

    model = models.Album
    serializer_class = serializers.AlbumSerializer
    parser_classes = (JSONParser,)


class TrackViewSet(ModelViewSet):
    '''
    All CRUD APIs available for manipulating Track model objects.
    '''

    model = models.Track
    serializer_class = serializers.TrackSerializer
    parser_classes = (JSONParser,)

from rest_framework import serializers

from . import models


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Track serializer. All fields are available, however, we're
    replacing the Track.size and Track.time fields with string
    versions for easier reading. We could also expose the
    underlying model fields as well if clients wanted to use
    the raw values.
    '''

    size = serializers.Field(source='size_string')
    time = serializers.Field(source='time_string')

    class Meta:
        model = models.Track


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Show all the fields on an Album.
    '''
    # Provide a list of links to all tracks for a given album.
    tracks = serializers.HyperlinkedRelatedField(view_name='track-detail',
                                                 many=True)
    #tracks = TrackSerializer(many=True)

    class Meta:
        model = models.Album


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Show all the fields on an Artist
    '''
    # Provide a list of links to all albums associated with a particular
    # artist.
    albums = serializers.HyperlinkedRelatedField(view_name='album-detail',
                                                 many=True)
    #albums = AlbumSerializer(many=True)

    class Meta:
        model = models.Artist


class ImportSerializer(serializers.Serializer):
    '''
    Simple serializer that just adds the capability of uploading a file.
    This is also made available through the browseable API.
    '''
    file_upload = serializers.FileField()

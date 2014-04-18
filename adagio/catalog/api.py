from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.generics import (
    SingleObjectAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from . import (
    serializers,
    models,
    utils,
)


class ArtistList(ListCreateAPIView):
    '''
    List artist resources.

    # AND...

    We can use markdown in our documentation by simply providing
    it in the docstring of the API methods.
    '''
    model = models.Artist
    serializer_class = serializers.ArtistSerializer
    parser_classes = (JSONParser,)


class ArtistDetail(RetrieveUpdateDestroyAPIView):
    '''
    Artist detail.
    '''
    model = models.Artist
    serializer_class = serializers.ArtistSerializer
    parser_classes = (JSONParser,)


class AlbumList(ListCreateAPIView):
    '''
    List album resources.
    '''
    model = models.Album
    serializer_class = serializers.AlbumSerializer
    parser_classes = (JSONParser,)


class AlbumDetail(RetrieveUpdateDestroyAPIView):
    '''
    Album detail.
    '''
    model = models.Album
    serializer_class = serializers.AlbumSerializer
    parser_classes = (JSONParser,)


class TrackList(ListCreateAPIView):
    '''
    List track resources.
    '''
    model = models.Track
    serializer_class = serializers.TrackSerializer
    parser_classes = (JSONParser,)


class TrackDetail(RetrieveUpdateDestroyAPIView):
    '''
    Track details
    '''
    model = models.Track
    serializer_class = serializers.TrackSerializer
    parser_classes = (JSONParser,)


##
# NOTE:
#
# Using generics.SingleObjectAPIView (or any APIView from generics module)
# will allow us to manage the browseable API through custom fields. Check
# out the serializer used in this API to see how we're not tying the
# serializer to a model, but rather building it up ourselves very easily.
##
class CatalogImport(SingleObjectAPIView):
    '''
    POST only API that accepts a single file upload that must be a valid
    XML export from iTunes. The XML will be parsed and any track information
    found will be loaded into the database. **This has only been tested on
    OS X 10.9 using iTunes v11.1.5.**

    > NOTE: the import as written will attempt to find existing objects in the
    > database and create them if not found. This could take a while as no
    > optimizations have been made.

    **@param** {File} file_upload: The valid XML-based iTunes export you wish
    to import.
    '''

    serializer_class = serializers.ImportSerializer

    # Ignore code complexity issues
    def post(self, request, *args, **kwargs):  # NOQA
        if not request.FILES or 'file_upload' not in request.FILES:
            raise ParseError('file_upload field required.')
        fp = request.FILES['file_upload']

        # parse the catalog and build up the database objects
        try:
            catalog = utils.parse_catalog(fp)

            artist_count, album_count, track_count = 0, 0, 0

            for item in catalog:
                artist_obj, created = models.Artist.objects.get_or_create(
                    name=item['Artist'])
                if created:
                    artist_count += 1

                album_obj, created = models.Album.objects.get_or_create(
                    artist=artist_obj,
                    name=item['Album'],
                )
                if created:
                    album_count += 1

                track_obj, created = models.Track.objects.get_or_create(
                    album=album_obj,
                    name=item['Name'],
                    number=item.get('Track Number'),
                    disc_number=item.get('Disc Number'),
                    size=item['Size'],
                    time=item['Total Time']
                )
                if created:
                    track_count += 1

                genre = item.get('Genre', '')
                if genre or album_obj.genre is None:
                    album_obj.genre = genre

                year = item.get('Year')
                if year or album_obj.year is None:
                    album_obj.year = year
                album_obj.save()

        except Exception:
            raise

        # load it into the database
        return Response({
            'new_artists': artist_count,
            'new_albums': album_count,
            'new_tracks': track_count,
        })

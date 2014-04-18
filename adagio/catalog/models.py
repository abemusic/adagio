from django.conf import settings
from django.db import models


class Artist(models.Model):

    # The name of the artist.
    name = models.CharField(max_length=128)

    def __unicode__(self):
        '''
        String representation of an Artist.
        '''
        return self.name


class Album(models.Model):

    # The artist who's album this is.
    artist = models.ForeignKey('catalog.Artist', related_name='albums')

    # The name of the album.
    name = models.CharField(max_length=128)

    # The genre of the album. This could be an empty string.
    genre = models.CharField(max_length=64, blank=True)

    # Year the album released. This could be a null value.
    year = models.IntegerField(null=True)

    def __unicode__(self):
        '''
        String representation of an Album.
        '''
        return self.name


class Track(models.Model):

    # The album this track belongs to.
    album = models.ForeignKey('catalog.Album', related_name='tracks')

    # The name of the track.
    name = models.CharField(max_length=128)

    # The track number on the album. This could be a null value.
    number = models.IntegerField(null=True)

    # If a multi-disc album, the disc number the track is on. This could be
    # a null value.
    disc_number = models.IntegerField(null=True)

    # Size of the track in bytes.
    size = models.IntegerField()

    # Total time of the track in milliseconds
    time = models.IntegerField()

    def __unicode__(self):
        '''
        String representation of a Track.
        '''
        return self.name

    @property
    def size_string(self):
        '''
        Converts the raw size value into human readable string (e.g, 10.1 MB)
        '''
        return '{0:.1f} MB'.format((self.size / 1048576.0))

    @property
    def time_string(self):
        '''
        Converts the raw time value into human readable string (e.g, 4:32)
        '''
        return '{0}:{1:02d}'.format(
            self.time / 1000 / 60,
            int(round(self.time / 1000.0 % 60))
        )

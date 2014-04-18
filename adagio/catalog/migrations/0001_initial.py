# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'catalog_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'catalog', ['Artist'])

        # Adding model 'Album'
        db.create_table(u'catalog_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='albums', to=orm['catalog.Artist'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'catalog', ['Album'])

        # Adding model 'Track'
        db.create_table(u'catalog_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tracks', to=orm['catalog.Album'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('disc_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('time', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'catalog', ['Track'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'catalog_artist')

        # Deleting model 'Album'
        db.delete_table(u'catalog_album')

        # Deleting model 'Track'
        db.delete_table(u'catalog_track')


    models = {
        u'catalog.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'albums'", 'to': u"orm['catalog.Artist']"}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'catalog.artist': {
            'Meta': {'object_name': 'Artist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'catalog.track': {
            'Meta': {'object_name': 'Track'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracks'", 'to': u"orm['catalog.Album']"}),
            'disc_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['catalog']
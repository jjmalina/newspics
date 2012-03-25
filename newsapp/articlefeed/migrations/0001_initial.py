# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Image'
        db.create_table('articlefeed_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=255)),
            ('image_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date_downloaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('articlefeed', ['Image'])

        # Adding model 'Article'
        db.create_table('articlefeed_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('author_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_downloaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('articlefeed', ['Article'])

        # Adding model 'Topic'
        db.create_table('articlefeed_topic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topics', to=orm['articlefeed.Article'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topics', to=orm['articlefeed.Image'])),
            ('date_downloaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('articlefeed', ['Topic'])


    def backwards(self, orm):
        
        # Deleting model 'Image'
        db.delete_table('articlefeed_image')

        # Deleting model 'Article'
        db.delete_table('articlefeed_article')

        # Deleting model 'Topic'
        db.delete_table('articlefeed_topic')


    models = {
        'articlefeed.article': {
            'Meta': {'object_name': 'Article'},
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_downloaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articles'", 'symmetrical': 'False', 'through': "orm['articlefeed.Topic']", 'to': "orm['articlefeed.Image']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '255'})
        },
        'articlefeed.image': {
            'Meta': {'object_name': 'Image'},
            'date_downloaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '255'}),
            'image_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'articlefeed.topic': {
            'Meta': {'object_name': 'Topic'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'to': "orm['articlefeed.Article']"}),
            'date_downloaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'to': "orm['articlefeed.Image']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['articlefeed']

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Topic.article'
        db.alter_column('articlefeed_topic', 'article_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['articlefeed.Article']))

        # Changing field 'Topic.image'
        db.alter_column('articlefeed_topic', 'image_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['articlefeed.Image']))


    def backwards(self, orm):
        
        # Changing field 'Topic.article'
        db.alter_column('articlefeed_topic', 'article_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['articlefeed.Article']))

        # Changing field 'Topic.image'
        db.alter_column('articlefeed_topic', 'image_id', self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.date(2012, 3, 25), to=orm['articlefeed.Image']))


    models = {
        'articlefeed.article': {
            'Meta': {'object_name': 'Article'},
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_downloaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'has_topics_and_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articles'", 'symmetrical': 'False', 'through': "orm['articlefeed.Topic']", 'to': "orm['articlefeed.Image']"}),
            'parsely_topics': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
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
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'null': 'True', 'to': "orm['articlefeed.Article']"}),
            'date_downloaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'null': 'True', 'to': "orm['articlefeed.Image']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['articlefeed']

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Type'
        db.create_table('publications_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('bibtex_types', self.gf('django.db.models.fields.CharField')(default='article', max_length=256)),
            ('hidden', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('publications', ['Type'])

        # Adding model 'Publication'
        db.create_table('publications_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publications.Type'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=4)),
            ('month', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('journal', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('book_title', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('volume', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pages', self.gf('publications.fields.PagesField')(max_length=32, blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('code', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('doi', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('external', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('publications', ['Publication'])


    def backwards(self, orm):
        # Deleting model 'Type'
        db.delete_table('publications_type')

        # Deleting model 'Publication'
        db.delete_table('publications_publication')


    models = {
        'publications.publication': {
            'Meta': {'ordering': "['-year', '-month', '-id']", 'object_name': 'Publication'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'book_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'code': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'doi': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'external': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pages': ('publications.fields.PagesField', [], {'max_length': '32', 'blank': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publications.Type']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'volume': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4'})
        },
        'publications.type': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Type'},
            'bibtex_types': ('django.db.models.fields.CharField', [], {'default': "'article'", 'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['publications']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Production'
        db.create_table(u'product_production', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['category.Category'])),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('stock', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'product', ['Production'])


    def backwards(self, orm):
        # Deleting model 'Production'
        db.delete_table(u'product_production')


    models = {
        u'category.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['category.Category']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '1'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'product.production': {
            'Meta': {'object_name': 'Production'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['category.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'stock': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['product']
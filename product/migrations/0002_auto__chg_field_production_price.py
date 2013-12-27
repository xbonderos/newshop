# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Production.price'
        db.alter_column(u'product_production', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'Production.price'
        db.alter_column(u'product_production', 'price', self.gf('django.db.models.fields.FloatField')())

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
            'Meta': {'ordering': "['name']", 'object_name': 'Production'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['category.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'stock': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['product']
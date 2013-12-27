# coding=utf-8
from django.db import models
from django.utils.translation import gettext as _
from category.models import Category


class Production(models.Model):
    name = models.CharField(_('Name of product'), max_length=255)
    category = models.ForeignKey(Category, verbose_name=_('Category'),)
    price = models.DecimalField(_('Price'), max_digits=19, decimal_places=2)
    stock = models.IntegerField(_('Stock'))

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __unicode__(self):
        return self.name


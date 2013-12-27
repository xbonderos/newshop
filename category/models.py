# coding=utf-8
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import mptt
from django.utils.translation import gettext as _


class Category(MPTTModel):
    STATUS_CHOICES = (
        ('1', _('Hidden')),
        ('2', _('Published')),
    )

    name = models.CharField(_('Category'), max_length=128)
    parent = TreeForeignKey('self', verbose_name=_('Category parent'), null=True, related_name='children', blank=True)
    status = models.CharField(max_length=1, default=1, choices=STATUS_CHOICES)
    description = models.TextField(_('Category description'), blank=True)


    class Meta:
        ordering = ["name"]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    class MPTTMeta:
        order_insertion_by = ['name']
        parent_attr = 'parent'


    def __unicode__(self):
        return self.name


mptt.register(Category, )

#from django_autoslug.fields import AutoSlugField

#slug = AutoSlugField(_('Category slug'), populate_from=('name',), recursive='parent', unique=True, max_length=255,
#                     overwrite=True, blank=True)

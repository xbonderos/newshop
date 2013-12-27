from django.contrib import admin
from django.utils.translation import gettext as _
from category.models import Category
from feincms.admin import tree_editor


class CategoryModelAdmin(tree_editor.TreeEditor):
    list_display = ['name', 'status', ]
    ordering = ['name']
    active_toggle = tree_editor.ajax_editable_boolean('active', _('active'))
    actions = ['make_published', 'make_hidden']

    def make_hidden(self, request, queryset):
        queryset.update(status='1')
    make_hidden.short_description = _('Hide selected category')

    def make_published(request, queryset):
        queryset.update(status='2')
    make_published.short_description = _('Publish selected categories')


admin.site.register(Category, CategoryModelAdmin)

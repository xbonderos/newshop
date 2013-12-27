from django.contrib import admin
from product.models import Production


class ProductionModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'stock', 'price']
    ordering = ['name']


admin.site.register(Production, ProductionModelAdmin)

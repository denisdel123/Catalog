from django.contrib import admin

from catalogApp.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price_for_pcs', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


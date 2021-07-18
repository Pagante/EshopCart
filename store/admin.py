from django.contrib import admin
from .models import Product, BestProduct, TrendingProduct, Variation
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name','price', 'stock', 'category','modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    list_display_links = ('id', 'product_name', 'price', 'stock')


class BestProductAdmin(admin.ModelAdmin):
    list_display =('best_name', 'description','is_available')


class TrendingProductAdmin(admin.ModelAdmin):
    list_display=('trend_name', 'slug', 'description')


class VariationAdmin(admin.ModelAdmin):
    list_display  = ('id','product', 'variation_category', 'variation_value' ,'is_active')
    list_display_links = ('id','product', 'variation_category', 'variation_value' )
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value' )


admin.site.register(Product, ProductAdmin)
admin.site.register(BestProduct, BestProductAdmin)
admin.site.register(TrendingProduct,TrendingProductAdmin)
admin.site.register(Variation, VariationAdmin)

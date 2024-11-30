from django.contrib import admin
from .models import Product, ProductImage, OwnerContact

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'slug', 'is_new_stock', 'created_at')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('is_new_stock', )
    search_fields = ('name', 'description')


    # def main_image_preview(self,obj):
    #     main_obj = obj.images.filter
@admin.register(OwnerContact)
class OwnerContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'mobile_number', 'whatsapp']

admin.site.register(ProductImage) 

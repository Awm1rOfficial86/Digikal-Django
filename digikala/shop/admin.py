from django.contrib import admin

from shop.models import *


# Register your models here.
class colorAdmin(admin.TabularInline):
    model = Color
    extra = 1


class optionAdmin(admin.TabularInline):
    model = Option
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [colorAdmin, optionAdmin]


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(SliderItem)
admin.site.register(News)
admin.site.register(Advertising1)
admin.site.register(Advertising2)
admin.site.register(Garanti)
admin.site.register(Bime)
admin.site.register(Owner_Product)

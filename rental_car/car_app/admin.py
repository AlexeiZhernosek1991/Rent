from django.contrib import admin
from .models import *


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_model', 'slug', 'category', 'register_num')
    list_display_links = ('id', 'category')
    list_filter = ('category', 'type_fuel')
    prepopulated_fields = {"slug": ("car_model",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Car, CarAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color)
admin.site.register(Body_type)
admin.site.register(Photo)
admin.site.register(Transmission)
admin.site.register(Type_fuel)
admin.site.register(Order)

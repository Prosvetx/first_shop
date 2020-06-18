from django.contrib import admin

from .models import *


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','product')





admin.site.register(ShippingAddress)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Image, ImageAdmin)

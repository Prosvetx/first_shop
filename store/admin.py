from django.contrib import admin

from .models import *

#class ShoppingAddressAdmin(admin.ModelAdmin):

     #fields = ('address')


admin.site.register(ShippingAddress)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)


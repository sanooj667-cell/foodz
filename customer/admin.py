from django.contrib import admin

from customer.models import Customer, CartItem, Address




admin.site.register(Customer)
admin.site.register(CartItem)
admin.site.register(Address)




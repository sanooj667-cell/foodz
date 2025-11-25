from django.contrib import admin

from customer.models import Customer, CartItem, Address, Bill




admin.site.register(Customer)
admin.site.register(CartItem)
admin.site.register(Address)
admin.site.register(Bill)






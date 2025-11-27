from django.contrib import admin

from customer.models import Customer, CartItem, Address, Bill, Order, Order_items




admin.site.register(Customer)
admin.site.register(CartItem)
admin.site.register(Address)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Order_items)







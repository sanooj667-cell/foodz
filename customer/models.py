from django.db import models
from users.models import User
from restaurent.models import Store, FoodItems


ORDER_STATUS_CHOICES = [
    ("PENDING", "Pending"),
    ("CONFIRMED", "Confirmed"),
    ("PREPARING", "Preparing"),
    ("READY", "Ready for Pickup"),
    ("OUT_FOR_DELIVERY", "Out For Delivery"),
    ("DELIVERED", "Delivered"),
    ("CANCELLED", "Cancelled"),
]




class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return self.user.email



class CartItem(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
    amount = models.IntegerField()
    quantity = models.IntegerField() 



    class Meta:
        db_table = 'cart'
        verbose_name = 'cart'
        verbose_name_plural = "cart"
        ordering = ['-id']

    def __str__(self):
        return self.item.name

    
    
    
class Address(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True, blank=True)
    longitude = models.CharField(max_length=100 , null=True,blank=True)
    latitude =  models.CharField(max_length=100 , null=True,blank=True)
    address =  models.CharField(max_length=255)
    appartment = models.CharField(max_length=100)
    landmark = models.CharField(max_length=255)
    address_type = models.CharField(max_length=255) 
    is_selected = models.BooleanField(default=False)


    class Meta:
        db_table = 'address'
        verbose_name = 'address'
        verbose_name_plural = "address"
        ordering = ['-id']

    def __str__(self):
        return self.address
    


class Bill(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True, blank=True)
    sub_totel = models.IntegerField()
    offer_price = models.IntegerField(default=0)   
    delivary_charge = models.IntegerField(default=0)
    totel = models.IntegerField()

    class Meta:
        db_table = 'bill'
        verbose_name = 'bill'
        verbose_name_plural = "bills"
        ordering = ['-id']

    def __str__(self):
        return f"Bill #{self.id} - ₹{self.totel}"







class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True,blank=True)

    offer_price = models.FloatField()   
    delivary_charge = models.FloatField()
    totel = models.FloatField()
    sub_totel =  models.FloatField()

    order_id = models.CharField(max_length=255)
    status =  models.CharField(max_length=255, choices=ORDER_STATUS_CHOICES)


    class Meta:
        db_table = 'order'
        verbose_name = 'order'
        verbose_name_plural = "orders"
        ordering = ['-id']

    def __str__(self):
        return str(self.order_id)

    

class Order_items(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='order_item')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodItems, on_delete=models.CASCADE)

    qty = models.IntegerField()
    amnt = models.FloatField()


    class Meta:
        db_table = 'order_item'
        verbose_name = 'order_item'
        verbose_name_plural = "order_items"
        ordering = ['-id']

    def __str__(self):
        return str(f"{self.product.name}---{self.order.order_id}")

        
    



    


    



    
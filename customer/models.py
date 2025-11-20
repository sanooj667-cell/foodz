from django.db import models
from users.models import User
from restaurent.models import Store, FoodItems



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
    longitude = models.CharField(max_length=100 , null=True,blank=True)
    latitude =  models.CharField(max_length=100 , null=True,blank=True)
    address =  models.CharField(max_length=255)
    appartment = models.CharField(max_length=100)
    landmark = models.CharField(max_length=255)

    
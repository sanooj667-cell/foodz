from django.db import models

class Storecategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='category')




    class Meta:
        db_table = 'restaurent_store_category'
        verbose_name = 'store category'
        verbose_name_plural = "store categories"
        ordering = ['-id']

    def __str__(self):
        return self.name
    



class Store(models.Model):
    name = models.CharField(max_length=100)
    catagorey =models.ForeignKey(Storecategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store')
    tagline = models.CharField(max_length=255)
    rating = models.FloatField()
    time = models.IntegerField()

    class Meta:
        db_table = 'restaurent_store'
        verbose_name = 'store'
        verbose_name_plural = "stories"
        ordering = ['-id']

    def __str__(self):
        return self.name
    

class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider')
    store = models.ForeignKey(Store ,on_delete=models.CASCADE)
 

    class Meta:
        db_table = 'restaurent_slider'
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'
        ordering = ['-id']


    def __str__(self):
        return self.name  
    


class FoodCatagory(models.Model):
    name = models.CharField(max_length=255)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)

    class Meta:
        db_table = 'food_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['-id']


    def __str__(self):
        return self.name  
    







class FoodItems(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='fooditem')
    price = models.IntegerField()
    category = models.ForeignKey(FoodCatagory, on_delete=models.CASCADE, related_name="food_items")
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    is_veg = models.BooleanField(default=False)


    class Meta:
        db_table = 'food_items'
        verbose_name = 'items'
        verbose_name_plural = 'items'
        ordering = ['-id']


    def __str__(self):
        return self.name  
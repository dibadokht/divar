from django.db import models

class City(models.Model):
    
    name = models.CharField(max_length=100 , unique=True)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    
    name = models.CharField(max_length=100 , unique=True)
    def __str__(self):
        return self.name
    
    
class Ad(models.Model):
    title = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    city = models.ForeignKey('City' , on_delete=models.PROTECT)
    category = models.ForeignKey('Category' , on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.title} ({self.city})"
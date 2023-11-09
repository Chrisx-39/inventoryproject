from django.db import models
from typing import Self
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food','Food'),

)


class Products(models.Model):
    name = models.CharField(max_length=100,null=True)
    brand = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null= True)
    category = models.CharField(max_length=20, choices=CATEGORY)
    quantity = models.PositiveIntegerField(null=True)


    class Meta:
        verbose_name_plural = 'Product'
        
    def __str__(self):
         return f'{self.name}-{self.quantity}-{self.brand}-{self.model}'

class Order(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User, models.CASCADE,null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date =  models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Order'

    def __str__ (self):
            return f' {self.product} ordered by {self.staff.username}  '
    
class Plant(models.Model):
     
    fleet_code = models.CharField(max_length=20, null=True)
    plant_name = models.CharField(max_length=100,null=True)
    mileage = models.PositiveBigIntegerField(null= True)
    comments = models.CharField(max_length=100,null=False)
     
    class Meta:
        verbose_name_plural = 'Plant'
        
    def __str__ (self):
          return f' {self.fleet_code}-{self.plant_name} '

from django.db import models

# Create your models here.
from django.db import models
from .models import *
from django.urls import reverse

from technoapp.models import mobiles,categ

# Create your models here.
class cartlist(models.Model):
    cart_id=models.CharField(max_length=200,unique=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class cartitem(models.Model):
    mob2=models.ForeignKey(mobiles,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quantity=models.IntegerField(max_length=100)
    active=models.BooleanField(default=True)

    def total(self):
        return self.mob2.price*self.quantity

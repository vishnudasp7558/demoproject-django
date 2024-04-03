from django.db import models
from shop.models import product
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    dete_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name

class order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_items= models.IntegerField()
    phone=models.BigIntegerField(default=0)
    address=models.TextField()
    order_date= models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(max_length=30,default='pending')
    delivery_status=models.CharField(max_length=20,default='pending')

    def __str__(self):
        return self.user.username

class account(models.Model):
    acctnum=models.BigIntegerField()
    accttype=models.CharField(max_length=20)
    amount=models.IntegerField()

    def __str__(self):
        return str(self.acctnum)


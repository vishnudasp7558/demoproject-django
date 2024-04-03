from django.db import models

# Create your models here.
class Shop(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to='shop/image',null=True,blank=True)

    def __str__(self):
        return self.name


class product(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to='product/image',null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Shop,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
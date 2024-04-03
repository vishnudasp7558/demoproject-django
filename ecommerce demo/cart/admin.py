from django.contrib import admin
from cart.models import Cart,order,account
# Register your models here.
admin.site.register(Cart)
admin.site.register(order)
admin.site.register(account)
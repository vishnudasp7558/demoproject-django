from django.shortcuts import render
from django.http import Httprespose
from shop.models import product
from cart.models import Cart,order,account
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def cartview(request):
    u=request.user
    c=Cart.objects.filter(user=u)
    total=0
    for i in c:
        total = total+i.quantity*i.product.price
    return render(request,'addcart.html',{'c':c,'total':total })

@login_required
def addcart(request,p):
    p=product.objects.get(id=p)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if(p.stock>0):
            cart.quantity+=1
            cart.save()
            p.stock-=1
            p.save()
    except:
        if(p.stock>0):
            cart=Cart.objects.create(product=p,user=u,quantity=1)
            cart.save()
            p.stock-= 1
            p.save()

    return cartview(request)

def remove(request,p):
    p = product.objects.get(id=p)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        if (cart.quantity> 1):
            cart.quantity -= 1
            cart.save()
            p.stock += 1
            p.save()
        else:
            cart.delete()
            p.stock +=1
            p.save()
    except:
        pass
    return cartview(request)


def full_remove(request,p):
    p = product.objects.get(id=p)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        cart.delete()
        p.stock+= cart.quantity
        p.save()
    except:
        pass

    return cartview(request)
@login_required
def orderform(request):
    if(request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']

        u=request.user

        c=Cart.objects.filter(user=u)

        total=0
        for i in c:
            total=total+i.quantity*i.product.price

        try:
            ac=account.objects.get(acctnum=n)
            if(ac.amount >= total):
                ac.amount=ac.amount-total
                print(ac.amount)
                ac.save()
                for i in c:
                    o=order.objects.create(user=u,product=i.product,address=a,phone=p,no_of_items=i.quantity,order_status="paid")
                    o.save()
                c.delete()

                msg="order placed successfully"
                print(msg)

                return render(request, 'orderdetails.html', {'message':msg})
            else:
                msg="insufficient balance"
                print(msg)
                return render(request, 'orderdetails.html', {'message':msg})

        except:
            pass

    return render(request,'orderform.html')

def orderdetails(request):
    return render(request,'orderdetails.html')

@login_required
def yourorder(request):
    u=request.user
    o=order.objects.filter(user=u)
    return render(request,'yourorder.html' ,{'o':o,'u':u.username})








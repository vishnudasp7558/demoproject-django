from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models import Shop,product
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def allcategories(request):
    c=Shop.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c=Shop.objects.get(id=p)
    p=product.objects.filter(category=c)
    return render(request, 'product.html',{'p':p,'c':c})


def details(request,p):
    p=product.objects.get(id=p)

    return render(request, 'detail.html',{'p':p })

def user_login(request):
    if(request.method=='POST'):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return HttpResponse("Invalid Creditails")


    return render(request,'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('shop:allcat')

def register(request):

    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        c=request.POST['c']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        if(c==p):
            user=User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            user.save()
            return redirect('shop:allcat')
        else:
            return HttpResponse("password are not same")


    return render(request, 'register.html')




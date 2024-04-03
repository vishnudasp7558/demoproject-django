from django.shortcuts import render
from shop.models import product
from django.db.models import Q
# Create your views here.
def searchproducts(request):
    p=None
    q=""
    if (request.method=="POST"):
        query=request.POST['q']
        if query:
            p=product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request,'searchproduct.html',{'p':p,'q':query})


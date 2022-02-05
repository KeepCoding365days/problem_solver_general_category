from django.shortcuts import render
from .models import upload
# Create your views here.
def upload_view(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            new_name=request.POST.get('name')
            new_category=request.POST.get('category')
            new_price=request.POST.get('price')
            new_code=request.POST.get('code')
            new_origin=request.user.last_name
            owner=request.user.username
            sale=request.POST.get('sale')
            if sale=="sale":
                sale=True
            else:
                sale=False
            upload.objects.create(name=new_name,category=new_category,price=new_price,code=new_code,origin=new_origin,for_sale=sale,new_owner=owner)
        return render(request,"upload.html",{})
    else:
        return render(request,"failed.html",{})

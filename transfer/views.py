from django.shortcuts import render
from upload.models import upload
from .models import transactions
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import check_password
# Create your views here.
def transfer_view(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            prod_id=request.POST.get("id")
            customer=request.POST.get("customer")
            price=request.POST.get("price")
            password=request.POST.get("password")
            prod=upload.objects.get(code=prod_id)
            if prod.new_owner==request.user.username:
                own=True
            else:
                own=False

            verify=check_password(password, request.user.password)

            lis=User.objects.all()
            for i in lis:
                if i.username==customer:
                    exist=True
                    break
                else:
                    exist=False
            if prod.for_sale==True and exist and own and verify :
                prod.new_owner=customer
                prod.new_price=price
                transactions.objects.create(buyer=customer,seller=request.user.username,price=price,code=prod_id)
                prod.save()
            else:
                return render(request,"failed.html",{})
    return render(request,"transfer.html",{})



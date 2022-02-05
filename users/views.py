from django.shortcuts import render
from django.contrib.auth.models import User
from upload.models import upload
# Create your views here.
def register_view(request):
    if request.method=="POST":
        name=request.POST.get('name')
        company_name=request.POST.get('company_name')
        password=request.POST.get('password')
        a=User.objects.create_user(name,'',password)
        a.last_name=company_name
        a.save()
    return render(request,"register.html",{})
def home(request):
    a=request.user.username
    lis=upload.objects.filter(new_owner=a)

    return render (request,"home.html",{"data":lis})
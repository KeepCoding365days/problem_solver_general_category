from django.shortcuts import render
from upload.models import upload
from transfer.models import transactions
# Create your views here.
def check(request):
    if request.method=="POST":
        id=request.POST.get("code")
        lis=upload.objects.all()
        a=transactions.objects.filter(code=id)

        for n in lis:
            if n.code==id:
                context={"prod":n,"data":a}
                return render(request,"result.html",context)
            else:

                return render(request,"failed.html",context)

    return render(request,"check.html",{})
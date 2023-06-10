from django.shortcuts import render,redirect
from . models import plant,comment





# Create your views here.


def about2(request):
    iname=request.GET['id']
    obj=plant.objects.get(id=iname)
    
    return render(request,'about.html',{'data':obj})




def cmt(request):
    imsg=request.GET['cmtmsg']
    iname=request.GET['user']
    id=request.GET['proid']

    obj=comment.objects.create(user=iname,msg=imsg,pro_id_id=id,like=0)
    obj.save()
    return redirect('/product/?id='+id)


def like(request):
    return render(request,'text.html')



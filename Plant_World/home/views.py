from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import auth
from django.contrib.auth.models import User
from product.models import plant

# Create your views .
def index(request):
    obj=plant.objects.all()
    return render(request,"index.html",{'data':obj}) 

def click(request):
    return render(request,"text.html",{'val':'java'})

def about(request):
    return render(request,'about.html')




def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pword=request.POST['pword' ]
        user=auth.authenticate(username=uname,password=pword)
        if user:
            auth.login(request,user)
            return redirect('/')
        msg='invalid user name and password'  
        return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')


def register(request):
    if request.method=='POST':
      uname=request.POST['uname']
      fname=request.POST['fname']
      lname=request.POST['lname']
      email=request.POST['email']
      pword=request.POST['pword']
      rpword=request.POST['rpword']
      if pword==rpword:
            if User.objects.filter(username=uname):
                msg="username is already taken"
                return render(request,'register.html',{'val':msg})
            elif User.objects.filter(email=email):
                msg="email is already taken"
                return render(request,'register.html',{'val':msg})
            
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pword) 
                user.save();
                auth.login(request,user) 
                return redirect("/")
                
      else:
            msg="invalid password"
            return render(request,'register.html',{'val':msg})
    else:
        return render(request,"register.html") 
    

def logout(request):
    auth.logout(request)
    return redirect('/')




    


         


    


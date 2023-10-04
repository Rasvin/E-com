from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import Category,Product

# Create your views here.
def index(request):
    category=Category.objects.filter(status=0)
    return render(request,'index.html',{"category":category})



def loginn(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already exists")
            return redirect('register')
        else:
         user=User.objects.create_user(username=username,email=email,password=password)
         user.save();
        return redirect('/')
    else:
        return render(request,'register.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')    



def Mobile(request,name):
    if(Category.objects.filter(name=name,status=0)):
        product=Product.objects.filter(Category__name=name)
    else:
        messages.info(request,"no")
        return redirect('/')
    return render(request,'Mobile.html',{"product":product})

def det(request,cate_name,prod_name):
    if(Category.objects.filter(name=cate_name,status=0)):
        if(Product.objects.filter(name=prod_name,status=0)):
            pcrt=Product.objects.filter(name=prod_name,status=0)
        else:
            messages.error(request,"no such product")
            return redirect('Mobile')            
    else:
        messages.error(request,"no such category")        
        return redirect('Mobile')
    return render(request,"det.html",{"pcrt":pcrt})
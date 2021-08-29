from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import userform
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def userlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        
        if user is not None:
            login (request,user)
            return redirect('/')
        else :
            messages.info(request,'Username or password in not valid')

    return render(request,'login.html')
def register(request):
    form=userform()
    if request.method == 'POST':
        form=userform(request.POST)
        if form.is_valid ():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, user + 'is successfully created')   
            return redirect('login')
         

    return render(request,'register.html',{'form':form})


def userlogout(request):
    logout(request)
    return redirect('/')    
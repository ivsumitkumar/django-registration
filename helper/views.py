from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def homePage(request):
    return render(request,'home.html')

def logInPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passwd = request.POST.get('pass')
        user = authenticate(request,username=uname,password=passwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username or password is incorrect!')
    
    return render(request,'login.html')

def sighUpPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        # pass1 = request.POST.get('password1')
        # pass2 = request.POST.get('password2')
        while True:    
            try:
                pass1 = request.POST.get('password1')
                pass2 = request.POST.get('password2')
                if pass1 != pass2:
                    raise Exception()
                else:
                    break
            except:
                return HttpResponse("Passoword not matched!")
        
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        return redirect('login')
    
    return render(request,'signup.html')
def LogOutPage(request):
    logout(request)
    return redirect('login')
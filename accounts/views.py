
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('user logged')
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            print('invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        name=request.POST['name']

        email = request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User name is alredy exist!!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is alredy exist!!")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=name,email=email,password=password1)
                user.save()
                messages.info(request,"Registration completed successfully")
                return redirect('/')

        else:
            messages.info(request, "Password did't match!!")
            return redirect('/')
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')
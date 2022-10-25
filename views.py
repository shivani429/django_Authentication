from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from itsdangerous import Serializer
from demoapp.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url='login')
def home(request):
       return render(request, 'home.html')   

#Authentication 
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Incorrect Username or Password')
        return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('user')
            messages.success(request,'Account created for '+ 'user') 
            return redirect('login')

    context = {'form':form}
    return render(request,'register1.html',context)


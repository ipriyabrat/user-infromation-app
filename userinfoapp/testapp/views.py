 
from django.shortcuts import render,redirect
from testapp.models import UserInfo
from testapp.forms import UserInfoForm,UserSingupForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib  import messages

 
 
# Create your views here.

def home_view(request):
    return render(request,'testapp/home.html')

def dash_view(request):
    messages.success(request,'Welcome to Your Dashboard')
    return render(request,'testapp/dashbord.html')

@login_required
def retrive_view(request):
    if request.user.is_authenticated:
        user=request.user
    user_info=UserInfo.objects.filter(user=user)
    return render(request,'testapp/retrive.html',{'user_info':user_info})


def insert_view(request):
    if request.user.is_authenticated:
        user=request.user

    form= UserInfoForm()
    if request.method == 'POST':
        form= UserInfoForm(request.POST)
        if form.is_valid():
            fm=form.save(commit=False)
            fm.user=user
            fm.save()

        messages.success(request,'DATA ADDED SUCCESSFULLY')
        return redirect('/retrive')
    return render(request,'testapp/insert.html',{'form':form})


def delete_view(request,id):
    employee = UserInfo.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee = UserInfo.objects.get(id=id)
    form = UserInfoForm(instance = employee) #populate form with emp data
    if request.method == 'POST':
        form = UserInfoForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/retrive')
    return render(request,'testapp/update.html',{'form':form})








def logout_view(request):
    return render(request,'testapp/logout.html')

def signup_view(request):
    form = UserSingupForm()
    if request.method == 'POST':
        form = UserSingupForm(request.POST)
        user = form.save()
        user.set_password(user.password) #to hash password
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})




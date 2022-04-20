from django.shortcuts import render,HttpResponseRedirect
from .forms import UserRegistration
from .models import User
from django.contrib import messages
# Create your views here.

#This function will add new user and show list of users

def add_show(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['full_name']
            em=fm.cleaned_data['email']
            cn=fm.cleaned_data['contact_no']
            pw=fm.cleaned_data['password']
            reg = User(full_name=nm,email=em,contact_no=cn,password=pw)
            # fm.save()
            reg.save()
            
            messages.add_message(request, messages.SUCCESS,"You have successfully added new user!!")
            fm = UserRegistration()
    else:
        fm = UserRegistration()
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud}) 

def show_data(request):
    fm = UserRegistration()
    stud = User.objects.all()
    return render(request,'enroll/show.html',{'form':fm,'stu':stud})
#This function will edit and update data

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserRegistration(request.POST , instance=pi)
        if fm.is_valid:
            fm.save()
            messages.add_message(request, messages.SUCCESS,"Your profile is updated successfully!!!")
            fm = UserRegistration()
    else:
        pi = User.objects.get(pk=id)
        fm =  UserRegistration(instance=pi)
    return render(request,'enroll/updateuser.html',{'form':fm})



# This function will delete data from database

def delete_data(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


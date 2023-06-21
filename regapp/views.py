from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import suserreg 
import mysql.connector,mysql
from regapp.form import studentform
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template

from django.views import View


# Create your views here.
def home(request):
    return render(request,'regapp/home.html')
def printout(request):
    if 'search' in request.GET: 
        search=request.GET['search']
        #queryset=suserreg.objects.filter(First_name__icontains=search)
        multiple_search=Q(Q(First_name__icontains=search) | Q(Last_name__icontains=search) | Q(Sclass__icontains=search) | Q(board__icontains=search) | Q(Schoolname__icontains=search) | Q(phone_no__icontains=search))
        queryset=suserreg.objects.filter(multiple_search)
    else:    
        queryset=suserreg.objects.all()
    context={"queryset":queryset}
    return render(request,'regapp/print.html',context)
class  Viewpdf(View):
    def get(self,request,*args,**kwargs):
        pdf=pdf_convert(request,'regapp/pdf.html')
        return HttpResponse(pdf,content_type='aplication/pdf')

def editdata(request,id):   
    edit=suserreg.objects.get(id=id)    
    return render(request,'regapp/update.html',{"edit":edit})
def update(request,id):
    update=suserreg.objects.get(id=id)
    form=studentform(request.POST,instance=update)
    if form.is_valid():
        form.save()        
        messages.info(request,"Data updated Successfully")
        return render(request,'regapp/update.html',{"edit":update})
def deletedata(request,id): 
    item=suserreg.objects.get(id= id)
    item.delete()
    messages.info(request,"Item deleted Successfully...")
    return redirect('printout')    

def adminreg(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'user is already exists')
                return redirect('adminreg')
            else:
                user= User.objects.create_superuser(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                user.set_password(password)
                user.save()
                print("success")
                messages.info(request,'user register details saved SUCCEESFULLY')
                return redirect('adminreg')
        else:
            messages.info(request,'check your password')
            return redirect('adminreg')    
    else:
        print("this is not post method")  
        return render(request,'regapp/adminreg.html')        
            
def adminlog(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("success")
            return render(request,'regapp/userreg.html')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('adminlog')
        
    else:    
        return render(request,'regapp/adminlog.html')                 
            
def userreg(request):
    if request.method == 'POST':
        First_name=request.POST['First_name']
        Last_name=request.POST['Last_name']
        Sclass=request.POST['Sclass']
        Schoolname=request.POST['Schoolname']
        board=request.POST['board']
        phone_no=request.POST['phone_no']
        suser=suserreg(First_name=First_name,Last_name=Last_name,Sclass=Sclass,Schoolname=Schoolname,board=board,phone_no=phone_no)
        suser.save()
        print("success")
        messages.info(request,'Details saved Successfully')
        return redirect('userreg')
    return render(request,'regapp/userreg.html')   
        


conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='studreg')
mycursor=conn.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)        
    
#nhgnghgmgmj
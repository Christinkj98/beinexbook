from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone, dateformat

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def login(request):
    if request.method =='POST':
        
        if beinexusers.objects.filter(Username=request.POST['username'], Password=request.POST['password'],Designation="admin").exists():
           
            member=beinexusers.objects.get(Username=request.POST['username'], Password=request.POST['password'])
           
            request.session['usernametsid'] = member.id
            if request.session.has_key('usernametsid'):
                usernamets = request.session['usernametsid']
            
            else:
                usernamets1 = "dummy"
            mem=beinexusers.objects.get(id=usernamets)
            mem1 = beinexbooks.objects.all()
            return render(request,'admin.html',{'mem':mem,'mem1':mem1})
    return render(request, 'login.html')
    
def logout(request):
    if 'usernametsid' in request.session:
        request.session.flush()
        return redirect('/')
    else: 
        return redirect('/')
        
        
       
    
 
def booklist(request):
    mem = beinexbooks.objects.all()
    return render(request,'books.html',{'mem':mem}) 

def adminlist(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernamets = request.session['usernametsid']
            mem = beinexusers.objects.get(id=usernamets)
            mem1 = beinexbooks.objects.all()
            return render(request, 'admin.html',{'mem':mem,'mem1':mem1})
    else:
        return redirect('/')

def editbook(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernamets = request.session['usernametsid']
            if request.method == 'POST':
                date = dateformat.format(timezone.now(),'YmdHis')
                var = beinexbooks.objects.get(id=id)
                if int(date)-int(var.Timestamp) > 10:
                    var.Bookname = request.POST['name']
                    var.Author = request.POST['author']
                    var.Description = request.POST['description']
                    var.Timestamp = date
                    var.save()
                return redirect('adminlist')
        mem = beinexusers.objects.get(id=usernamets)
        mem1 = beinexbooks.objects.get(id=id)
        return render(request, 'edit.html',{'mem':mem,'mem1':mem1}) 
    else:
        return redirect('/') 
 
def deletebook(request,id):
    mem = beinexbooks.objects.get(id=id)
    mem.delete()
    return redirect('adminlist')

def addnew(request):
    if request.method == 'POST':
        mem = beinexbooks()
        mem.Bookname = request.POST['name']
        mem.Author = request.POST['author']
        mem.Description = request.POST['description']
        mem.save()
        return redirect('adminlist')
    return render(request, 'add.html') 
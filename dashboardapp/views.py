from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .filters import *
from .forms import *
from .models import *
# Create your views here.


#sign in route
def signin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')
                
        return render(request,'signin.html')


#sign up route
def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = signupForm()
        if request.method =='POST':
            form=signupForm(request.POST)
            name=request.POST.get('username')
            usernames=User.objects.all()
            for uname in usernames:
                if str(name) == str(uname):
                    messages.info(request, 'username is already exist try to sign up with other username')
                    break
            if form.is_valid():
                user=form.save()
                group = Group.objects.get(name="student")
                user.groups.add(group)
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)
                return redirect('signin')
        context={'form':form}
        return render(request,'signup.html',context)

#logout route
@login_required(login_url='signin')
def logoutUser(request):
	logout(request)
	return redirect('signin')

@login_required(login_url='signin')
def dashboard(request):
    images=Showcase.objects.all()[0]
    context={'dashboard':True,'images':images} 
    return render(request,'dashboard.html',context)

@login_required(login_url='signin')
def datalist(request,id):
    usertype=validfeild(str(request.user.groups.all()[0]),id)
    data=Datamodel.objects.filter(category = id)
    myfilter=dataFilter(request.GET,queryset=data)
    data=myfilter.qs
    # form=dataForm()
    # if request.method=='POST':
    #     csrfmiddlewaretoken=request.POST.get('csrfmiddlewaretoken')
    #     name=request.POST.get("name")
    #     description=request.POST.get("description")
    #     datafile=request.FILES.get("datafile")
    #     a={"csrfmiddlewaretoken":csrfmiddlewaretoken,"name":name,"category":id,"description":description}
    #     b={"datafile":datafile}
    #     form=dataForm(a,b)
    #     if form.is_valid():
    #         form.save()
    context={'data':data,"myfilter":myfilter,"usertype":usertype,"id":id}
    return render(request,'datalist.html',context)


def validfeild(group,id):
    if group == 'python':
        return '1'==id
    elif group == 'web':
        return '2'== id
    elif group == 'mobileapp':
        return '3'==id
    elif group == 'gcd':
        return '4'==id
    else:
        return False



@login_required(login_url='signin')
def createdata(request,id):
    form=dataForm()
    if request.method=='POST':
        csrfmiddlewaretoken=request.POST.get('csrfmiddlewaretoken')
        name=request.POST.get("name")
        description=request.POST.get("description")
        datafile=request.FILES.get("datafile")
        a={"csrfmiddlewaretoken":csrfmiddlewaretoken,"name":name,"category":id,"description":description}
        b={"datafile":datafile}
        form=dataForm(a,b)
        if form.is_valid():
            form.save()
            return redirect('/{}/{}'.format('data',id))
    context={"form":form}            
    return render(request,'createdata.html',context)


@login_required(login_url='signin')
def updatedata(request,id,cat):
    data=Datamodel.objects.get(id=id)
    form=dataForm(instance=data)
    if request.method=='POST':
        csrfmiddlewaretoken=request.POST.get('csrfmiddlewaretoken')
        name=request.POST.get("name")
        description=request.POST.get("description")
        datafile=request.FILES.get("Datafile")
        a={"csrfmiddlewaretoken":csrfmiddlewaretoken,"name":name,"category":cat,"description":description}
        b={"datafile":datafile}
        form=dataForm(a,request.FILES,instance=data)
        # form=dataForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/{}/{}'.format('data',cat))
    context={'form':form}
    return render(request,'createdata.html',context)

@login_required(login_url='signin')
def deletedata(request,id,cat):
    data=Datamodel.objects.get(id=id)
    if request.method=='POST':
        data.delete()
        return redirect('/{}/{}'.format('data',cat))

@login_required(login_url='signin')
def event(request,cat):
    events=DoneEvents.objects.filter(upcoming=bool(int(cat)))
    text = "Events done by us" if cat=='0' else "Upcoming Events"
    context={"events":events,'text':text}
    return render(request,'events.html',context)
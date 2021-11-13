from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import mobiles,categ
from  django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request,c_slug=None):
    c_page=None
    mob=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        mob=mobiles.objects.filter(category=c_page,availability=True)
    else:
        mob=mobiles.objects.all().filter(availability=True)
    c=categ.objects.all()

    paginator=Paginator(mob,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        mob=paginator.page(page)
    except(EmptyPage,InvalidPage):
        mob=Paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'cc': c, 'mobile': mob})
def register(request):
    if request.method =='POST':
        username=request.POST['name']
        passw=request.POST['password']
        email=request.POST['mail']
        cpass=request.POST['cpassword']
        if passw==cpass:
            user=User.objects.create_user(username=username,email=email,password=passw)
            user.save()
            messages.info(request,"success")
            return redirect('login')
        else:
            messages.info(request,"password missmatch")

    return  render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid username or password")
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def mobilehome(request,c_slug):
    m=mobiles.objects.get(slug=c_slug)
    return render(request,'mobiles.html',{'mm':m})
def search1(request):
    prod=None
    query=None

    if 's' in request.GET:
        query=request.GET.get('s')
        prod=mobiles.objects.all().filter(Q(mobname__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'abc':prod})

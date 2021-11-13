from django.contrib import messages
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from .models import cartitem,cartlist
from technoapp.models import mobiles
from django.core.exceptions import ObjectDoesNotExist

def cartid(request):
    a=request.session.session_key
    if not a:
        a=request.session.create()
    return a


def add(request,id):
    m=mobiles.objects.get(id=id)
    try:
        ct=cartlist.objects.get(cart_id=cartid(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=cartid(request))
        ct.save()
    try:
        citem=cartitem.objects.get(mob2=m,cart=ct)
        if citem.quantity < citem.mob2.stock:
            citem.quantity+=1
        citem.save()

    except cartitem.DoesNotExist:
        citem=cartitem.objects.create(mob2=m,quantity=1,cart=ct)
        citem.save()
        messages.info(request,"success")
    return redirect('carthome')

def carthome(request,count=0,tot=0,ct_items=None):

    try:
         c=cartlist.objects.get(cart_id=cartid(request))
         ct_items=cartitem.objects.filter(cart=c,active=True)
         for i in ct_items:
            tot +=(i.mob2.price*i.quantity)
            count+=i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ci':ct_items,'t':tot})
def mincart(request,id):
    c=cartlist.objects.get(cart_id=cartid(request))
    m=get_object_or_404(mobiles,id=id)
    citem=cartitem.objects.get(mob2=m,cart=c)
    if citem.quantity > 1:
        citem.quantity-=1
        citem.save()
    else:
        citem.delete()
    return redirect('carthome')

def cartdelete(request,mobid):
    c=cartlist.objects.get(cart_id=cartid(request))
    m=get_object_or_404(mobiles,id=mobid)
    citem=cartitem.objects.get(mob2=m, cart=c)
    citem.delete()
    return redirect('carthome')

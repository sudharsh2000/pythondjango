from django.shortcuts import render, redirect
# from .models import cartitem,cartlist
from technoapp.models import mobiles
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# def cart_id(request):
#     # a=request.session.session_key
#     # if not a:
#     #     a=request.session.create()
#     return a
#
#
# def addcart(request,id):
#     # m=mobiles.objects.get(id=id)
#     # try:
#     #     c=cartlist.objects.get(cart_id=cart_id(request))
#     # except cartlist.DoesNotExist:
#     #     c=cartlist.objects.create(cart_id=cart_id(request))
#     #     c.save()
#     # try:
#     #     citem=items.objects.get(prod_id=m,cart_id=c)
#     #     if citem.quant < citem.m.stock:
#     #         citem.quant+=1
#     #         citem.save()
#     # except items.DoesNotExist:
#     #     citem.object.create(prod=m,quant=1,cart=c)
#     #     citem.save()
#     return redirect('/')
# def carthome(request):
#     # a=items.objects.all()
#
#     return render(request,'cart.html',)
# def cartdelete(request):
#     return redirect('/')



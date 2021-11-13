from .views import *
from .models import *
def count(requset):
    item_count=0
    if 'admin'in requset.path:
        return
    else:
        try:
            ct=cartlist.objects.filter(cart_id=cartid(requset))
            cc=cartitem.objects.all().filter(cart=ct[:1])
            for i in cc:
               item_count+=i.quantity
        except cartlist.DoesNotExist:

            item_count=0
        return dict(counter=item_count)
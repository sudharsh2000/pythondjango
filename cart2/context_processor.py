from .views import *
from .models import *
def count(request):
    item_count=0
    if 'admin'in request.path:
        return {}
    else:
        try:
            ct=cartlist.objects.filter(cart_id=cartid(request))
            cc=cartitem.objects.all().filter(cart=ct[:1])
            for i in cc:
               item_count+=i.quantity
        except cartlist.DoesNotExist:

            item_count=0
        return dict(counter=item_count)
from django.contrib import admin

from .models import cartlist,cartitem
# Register your models here.
admin.site.register(cartlist)
admin.site.register(cartitem)
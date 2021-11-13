from django.contrib import admin
from .models import categ,mobiles
# Register your models here.

class categadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,categadmin)

class mobileadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('mobname',)}
admin.site.register(mobiles,mobileadmin)
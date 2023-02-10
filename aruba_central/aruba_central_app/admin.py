from django.contrib import admin
from .models import Site, iap, switch, order
# Register your models here.


admin.site.register(Site) 
admin.site.register(iap)
admin.site.register(order)
admin.site.register(switch)


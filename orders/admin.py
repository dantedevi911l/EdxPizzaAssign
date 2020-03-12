from django.contrib import admin
from orders.models import Topping, Pizza, SubAddOn, Subs, Pasta, Salads, DinnerPlatters, Orders

# Register your models here.
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(SubAddOn)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(Orders)

from django.contrib import admin
from .models import Location, Store, Offer, User, Order, Payment, PaymentType

# Register your models here.
admin.site.register(Location)
admin.site.register(Offer)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(PaymentType)
admin.site.register(Store)

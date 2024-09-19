from django.contrib import admin
from .models import CustomerUser, Booking, Doctor, Availability

# Register your models here
admin.site.register(CustomerUser)
admin.site.register(Booking)
admin.site.register(Doctor)
admin.site.register(Availability)
# admin.site.register(Service)
# admin.site.register(Booking)

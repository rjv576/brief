from django.contrib import admin
from .models import Debt, PaymentMethod
# Register your models here.
admin.site.register(Debt)
admin.site.register(PaymentMethod)
admin.site.site_header = 'Debt Manager'

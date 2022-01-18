from django.contrib import admin
from .models import *

admin.site.register(Orders)
admin.site.register(Invoice)
admin.site.register(Statement)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Inventory)

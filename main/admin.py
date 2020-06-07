from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Drug)
admin.site.register(Entry)
admin.site.register(Lot)
admin.site.register(Client)
admin.site.register(Prescription)

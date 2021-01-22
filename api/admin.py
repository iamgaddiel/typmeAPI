from django.contrib import admin
from api.models import CustomUser, Prescription, Condition

admin.site.register(CustomUser)
admin.site.register(Condition)
admin.site.register(Prescription)

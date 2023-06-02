from django.contrib import admin
from .models import suserreg

# Register your models here.
class suserregadmin(admin.ModelAdmin):
    list_display=['id','First_name','Last_name','Sclass','Schoolname','board','phone_no']

admin.site.register(suserreg,suserregadmin)
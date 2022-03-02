from django.contrib import admin
from .models import customer
# Register your models here.
class customerAdmin(admin.ModelAdmin):
    list_display=["cid","cname","cadd","payment"]
    search_fields=["cid","cadd"]
    ordering=["payment"] #ascending order based on payment
    #ordering=["-payment"] #descending order
    list_filter=["cadd","payment"]
admin.site.register(customer,customerAdmin)

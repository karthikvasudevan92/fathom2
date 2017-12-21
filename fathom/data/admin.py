from django.contrib import admin
from .models import Prefix,Quantity,Unit,Term

# Register your models here.
admin.site.register(Prefix)
admin.site.register(Quantity)
class UnitAdmin(admin.ModelAdmin):
    list_filter = ('quantity',)
    filter_horizontal = ('terms',)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Term)

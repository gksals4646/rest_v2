from django.contrib import admin
from .models import Customer
from .models import ReservTime
from .models import Tables
from .models import Reservation
from .models import ReservState
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','phone',)

class ReservTimeAdmin(admin.ModelAdmin):
    list_display = ('time',)

class TableAdmin(admin.ModelAdmin):
    list_display = ('table',)

class ReservstateAdmin(admin.ModelAdmin):
    list_display = ('reserv',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('party','table','party_num','spot','time')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(ReservTime,ReservTimeAdmin)
admin.site.register(Tables,TableAdmin)
admin.site.register(ReservState, ReservstateAdmin)
admin.site.register(Reservation, ReservationAdmin)
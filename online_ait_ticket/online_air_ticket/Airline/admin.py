from django.contrib import admin
from .models import Connection, Feedback, Passangers

# Register your models here.


class CAdmin(admin.ModelAdmin):
    list_display = ['place_of_origin','place_of_destination','departure_time','arrival_time','date','price','no_of_seats','flight_number']


class FAdmin(admin.ModelAdmin):
    list_display = ['name','email','feedback']


class PAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','gender','birthdate','nationality','flight_id']


admin.site.register(Connection, CAdmin)
admin.site.register(Feedback, FAdmin)
admin.site.register(Passangers, PAdmin)

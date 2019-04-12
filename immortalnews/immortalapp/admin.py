from django.contrib import admin
from .models import *
# Register your models here.
class Hyd_jobs_Admin(admin.ModelAdmin):
    list_display = ['date','company','title','elegibility','address','email','contact']













admin.site.register(Hyd_jobs,Hyd_jobs_Admin)
admin.site.register(Blr_jobs)
admin.site.register(Chennai_jobs)
admin.site.register(Pune_jobs)


from django.contrib import admin
from .models import Hospital,MainDoctor,Doctor,Nurses,Patients


class HospitalAdmin(admin.ModelAdmin):
    list_display =("name","region",'gov','doctors','maxn')
    # search_fields= ("name","doctors","region")
    # list_editable = ("name","doctors")
    # list_filter = ("name", "region")

admin.site.register(Hospital,HospitalAdmin)

class MainDoctorAdmin(admin.ModelAdmin):
    list_display =("name","pin",'birthdate','phone')
    # search_fields= ("name","doctors","region")
    # list_editable = ("name","doctors")
    # list_filter = ("name", "region")

admin.site.register(MainDoctor, MainDoctorAdmin)


class NursesAdmin(admin.ModelAdmin):
    list_display =("name","pin",'birthdate','phone')
    # search_fields= ("name","doctors","region")
    # list_editable = ("name","doctors")
    # list_filter = ("name", "region")

admin.site.register(Nurses,NursesAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display =("position","pin",'birthdate','phone','hospital')
    # search_fields= ("name","doctors","region")
    # list_editable = ("name","doctors")
    # list_filter = ("name", "region")

admin.site.register(Doctor,DoctorAdmin)


class PatientsAdmin(admin.ModelAdmin):
    list_display =("name","pin",'birthdate','phone','reason','hospital','doctor')
    # search_fields= ("name","doctors","region")
    # list_editable = ("name","doctors")
    # list_filter = ("name", "region")

admin.site.register(Patients,PatientsAdmin)






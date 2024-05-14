from django.contrib import admin
from .models import Crime, Charge, Evidence, Investigation, Suspect, Victim, Witness

class CrimeAdmin(admin.ModelAdmin):
    list_display = ('reference', 'name', 'description', 'location', 'date_reported', 'time_reported','email')
    list_filter = ('date_reported', 'location','email')  
    search_fields = ('name', 'location', 'description','email')  

class ChargeAdmin(admin.ModelAdmin):
    list_display = ('description', 'reference')
    search_fields = ('description',)

class EvidenceAdmin(admin.ModelAdmin):
    list_display = ('description', 'reference')
    search_fields = ('description',)

class InvestigationAdmin(admin.ModelAdmin):
    list_display = ('lead_investigator', 'status', 'reference')
    search_fields = ('lead_investigator__username', 'status')

class SuspectAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'apprehended', 'reference')
    list_filter = ('apprehended',)
    search_fields = ('name', 'description')

class VictimAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'address', 'phone_number', 'reference')
    search_fields = ('name', 'address', 'phone_number')

class WitnessAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'address', 'phone_number', 'description', 'reference')
    search_fields = ('name', 'address', 'phone_number', 'description')

admin.site.register(Crime, CrimeAdmin)
admin.site.register(Charge, ChargeAdmin)
admin.site.register(Evidence, EvidenceAdmin)
admin.site.register(Investigation, InvestigationAdmin)
admin.site.register(Suspect, SuspectAdmin)
admin.site.register(Victim, VictimAdmin)
admin.site.register(Witness, WitnessAdmin)

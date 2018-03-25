from django.contrib import admin

from .models import Address, Dog, Event, Owner, Trial, TrialClass

admin.site.register(Owner, admin.ModelAdmin)
admin.site.register(Dog, admin.ModelAdmin)
admin.site.register(Event, admin.ModelAdmin)
admin.site.register(Address, admin.ModelAdmin)
admin.site.register(TrialClass, admin.ModelAdmin)
admin.site.register(Trial, admin.ModelAdmin)

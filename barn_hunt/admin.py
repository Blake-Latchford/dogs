from django.contrib import admin

from .models import Address, Dog, Event, Owner, Trial, TrialClass, CompetitionClass


class HiddenAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


admin.site.register(Owner, HiddenAdmin)
admin.site.register(Address, HiddenAdmin)
admin.site.register(CompetitionClass, HiddenAdmin)
admin.site.register(Trial, HiddenAdmin)

admin.site.register(Event)
admin.site.register(Dog)


class TrialClassAdmin(admin.ModelAdmin):
    model = TrialClass


admin.site.register(TrialClass, TrialClassAdmin)

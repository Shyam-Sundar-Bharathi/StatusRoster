from django.contrib import admin
from .models import Cluster, Member, Roster, Log, Status
from .signals import create_log

class RosterAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        user = request.user if request.user.is_authenticated else None
        super().save_model(request, obj, form, change)
        created = not change
        create_log(sender=Roster, instance=obj, created=created, user=user)


admin.site.register(Cluster)
admin.site.register(Member)
admin.site.register(Log)
admin.site.register(Status)
admin.site.register(Roster, RosterAdmin)
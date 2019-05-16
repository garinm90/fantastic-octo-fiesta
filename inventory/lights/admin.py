from django.contrib import admin

from .models import Light, LightLog

# Register your models here.
class LightAdmin(admin.ModelAdmin):
    exclude = ["slug"]


class LightLogAdmin(admin.ModelAdmin):
    readonly_fields = ("date_modified", "lights_before", "lights_after")


admin.site.register(Light, LightAdmin)
admin.site.register(LightLog, LightLogAdmin)

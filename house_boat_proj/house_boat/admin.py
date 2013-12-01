from django.contrib import admin
import house_boat.models as models


class BoatPhotoInline(admin.TabularInline):
    model = models.BoatPhoto


class BoatExtraInline(admin.TabularInline):
    model = models.BoatExtra


class BoatAdmin(admin.ModelAdmin):
    inlines = [
        BoatPhotoInline, BoatExtraInline
    ]

admin.site.register(models.Port)
admin.site.register(models.Boat, BoatAdmin)
admin.site.register(models.BoatExtra)
admin.site.register(models.BoatPhoto)

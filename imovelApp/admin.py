from django.contrib import admin
from imovelApp import models
from imovelApp.models import Client

# Register your models here.
admin.site.register(Client)
admin.site.register(models.RegisterLocation)


# admin.site.register(models.Immobile)
# admin.site.register(models.ImmobileImage)


class ImmobileImageInlineAdmin(admin.TabularInline):
    model = models.ImmobileImage
    extra = 0


class ImmobileAdmin(admin.ModelAdmin):
    inlines = [ImmobileImageInlineAdmin]


admin.site.register(models.Immobile, ImmobileAdmin)

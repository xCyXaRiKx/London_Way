from django.contrib import admin
from django.utils.html import format_html
from django.forms import widgets, ImageField
from django.utils.safestring import mark_safe
from U_stations.models import station, fact, image

class FactInline(admin.StackedInline):
    model = fact
    fields = ['name']
    readonly_fields = ['change_date']


class ImageAdminModel(admin.ModelAdmin, ImageField):
    model = image

    inlines = [FactInline]
    list_display = ['image_tag','alt_text', 'img', 'change_date']

class FactAdminModel(admin.ModelAdmin):
    model = fact
    list_display = ['name', 'image_tag', 'descr_format', 'create_date', 'change_date']

admin.site.register(station)
admin.site.register(fact, FactAdminModel)
admin.site.register(image, ImageAdminModel)
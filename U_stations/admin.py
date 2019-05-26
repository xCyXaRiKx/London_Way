from django.contrib import admin
from django.utils.html import format_html
from django.forms import widgets, ImageField
from django.utils.safestring import mark_safe
from U_stations.models import station, fact, image



class ImageAdminModel(admin.ModelAdmin, ImageField):
    model = image
    list_display = ('image_tag','alt_text', 'img', 'change_date')

admin.site.register(station)
admin.site.register(fact)
admin.site.register(image, ImageAdminModel)
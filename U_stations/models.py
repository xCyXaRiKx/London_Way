from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

class image(models.Model):
    img = models.ImageField(upload_to='images/%Y_%m_%d', null=True, blank=True)
    alt_text = models.CharField(max_length=200, default='Alt_text')
    change_date = models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.img.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.alt_text


class station(models.Model):
    name = models.CharField(verbose_name=u'Station name', max_length=100, null=False, default='Station_Name')
    description = models.TextField()
    #main_image = models.ForeignKey(upload_to='static/img/', on_delete='Cascade')
    additional_images = models.ManyToManyField(image)
    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)



class fact(models.Model):
    name = models.CharField(max_length=100, null=False, default='Fact_Name')
    short_description = models.TextField()
    main_text = models.TextField()
    main_image = models.ForeignKey(image, on_delete='Cascade')
    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)


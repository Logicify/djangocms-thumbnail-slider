from cms.models import CMSPlugin
from django.db import models


# Create your models here.
class ThumbnailSlider(CMSPlugin):
    enable_thumbnail_carousel = models.BooleanField(blank=False, null=False, default=False)
    items_on_slider = models.IntegerField(blank=True, null=False, default=1)
    additional_classes = models.CharField(blank=True, null=False, max_length=255, default='')
    slide_classes = models.CharField(blank=True, null=False, max_length=255, default='')
    thumbnail_width = models.IntegerField(blank=True, null=False, default=100)
    thumbnail_items = models.IntegerField(blank=True, null=False, default=10)

    def __str__(self):
        return "%s slides" % self.num_children()

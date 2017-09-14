from cms.models import CMSPlugin
from cmsplugin_filer_image.models import FilerImageField
from django.db import models


# Create your models here.
class ThumbnailSlider(CMSPlugin):
    additional_slider_classes = models.CharField(blank=True, null=True, max_length=255)
    additional_carousel_classes = models.CharField(blank=True, null=True, max_length=255)
    enable_thumbnail_carousel = models.BooleanField(blank=False, null=False, default=False)
    enable_embedded_carousel_styles = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return "%s slides" % self.num_children()


class ThumbnailSlide(CMSPlugin):
    image = FilerImageField(blank=True, null=True)
    link = models.CharField(blank=True, null=True, max_length=255)
    alt_text = models.CharField(blank=True, null=True, max_length=255)

    def get_url(self):
        if self.image:
            return self.image.url
        elif self.link:
            return self.link
        return None

    def __str__(self):
        return self.get_url()

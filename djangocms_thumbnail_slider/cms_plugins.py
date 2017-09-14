from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from djangocms_thumbnail_slider import models
from django.utils.translation import ugettext_lazy as _


# Create your plugins here
class ThumbnailSliderPlugin(CMSPluginBase):
    model = models.ThumbnailSlider
    module = _('Thumbnail slider')
    name = _('Slider')
    allow_children = True
    child_classes = ['ThumbnailSlidePlugin']
    render_template = 'thumbnail_slider/slider.html'


plugin_pool.register_plugin(ThumbnailSliderPlugin)


class ThumbnailSlidePlugin(CMSPluginBase):
    model = models.ThumbnailSlide
    module = _('Thumbnail slider')
    name = _('Slide')
    allow_children = True
    require_parent = True
    parent_classes = ['ThumbnailSliderPlugin']
    render_template = 'thumbnail_slider/slide.html'


plugin_pool.register_plugin(ThumbnailSlidePlugin)

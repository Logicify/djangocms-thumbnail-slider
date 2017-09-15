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
    child_classes = ['FilerImagePlugin']
    render_template = 'thumbnail_slider/slider.html'
    fieldsets = (
        (None, {
            'fields': [
                'enable_thumbnail_carousel',
                'items_on_slider'
            ]
        }),
        (_("Advanced settings"), {
            'classes': ('collapse',),
            'fields': [
                ('additional_classes', 'slide_classes'),
                ('thumbnail_width', 'thumbnail_items')
            ]
        })
    )

    def render(self, context, instance, placeholder):
        context = super(ThumbnailSliderPlugin, self).render(context, instance, placeholder)
        return context


plugin_pool.register_plugin(ThumbnailSliderPlugin)

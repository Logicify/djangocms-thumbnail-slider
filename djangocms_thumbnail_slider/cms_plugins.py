#    Thumbnail slider plugin for Django CMS
#    Copyright (C) 2017 Dmitriy Selischev
#    The MIT License (MIT)
#    
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#    
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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

# -*- coding: utf-8 -*-

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

from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbnailSlide',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='djangocms_thumbnail_slider_thumbnailslide', parent_link=True, to='cms.CMSPlugin')),
                ('link', models.CharField(max_length=255, blank=True, null=True)),
                ('alt_text', models.CharField(max_length=255, blank=True, null=True)),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ThumbnailSlider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='djangocms_thumbnail_slider_thumbnailslider', parent_link=True, to='cms.CMSPlugin')),
                ('additional_slider_classes', models.CharField(max_length=255, blank=True, null=True)),
                ('additional_carousel_classes', models.CharField(max_length=255, blank=True, null=True)),
                ('enable_thumbnail_carousel', models.BooleanField(default=False)),
                ('enable_embedded_carousel_styles', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

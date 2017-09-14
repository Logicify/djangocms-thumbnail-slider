# -*- coding: utf-8 -*-
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

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbnailSlider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='djangocms_thumbnail_slider_thumbnailslider', parent_link=True, to='cms.CMSPlugin')),
                ('enable_thumbnail_carousel', models.BooleanField(default=False)),
                ('items_on_slider', models.IntegerField(blank=True, default=1)),
                ('additional_classes', models.CharField(max_length=255, blank=True, default='')),
                ('slide_classes', models.CharField(max_length=255, blank=True, default='')),
                ('thumbnail_width', models.IntegerField(blank=True, default=100)),
                ('thumbnail_items', models.IntegerField(blank=True, default=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_thumbnail_slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnailslider',
            name='auto_play',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thumbnailslider',
            name='loop',
            field=models.BooleanField(default=False),
        ),
    ]

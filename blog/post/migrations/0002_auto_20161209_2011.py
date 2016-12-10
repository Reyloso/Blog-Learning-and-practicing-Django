# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='portada',
            field=models.ImageField(upload_to=b'covers', null=True, verbose_name=b'Cover', blank=True),
        ),
    ]

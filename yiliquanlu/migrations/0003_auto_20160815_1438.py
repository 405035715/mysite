# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yiliquanlu', '0002_fileupload'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='fileUpload',
            new_name='UploadText',
        ),
    ]
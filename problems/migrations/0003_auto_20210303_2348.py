# Generated by Django 3.1.6 on 2021-03-03 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_auto_20210303_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='name',
            new_name='title',
        ),
    ]

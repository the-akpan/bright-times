# Generated by Django 4.1.4 on 2022-12-24 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btl_logistics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='tracking_number',
            new_name='tracking_id',
        ),
    ]

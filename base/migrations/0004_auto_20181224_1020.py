# Generated by Django 2.1.4 on 2018-12-24 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20181224_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='telehpone',
            new_name='telehphone',
        ),
    ]

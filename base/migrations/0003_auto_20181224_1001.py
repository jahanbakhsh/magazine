# Generated by Django 2.1.4 on 2018-12-24 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20181224_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='postalcode',
            field=models.CharField(help_text='کد پستی دفتر مرکزی', max_length=12, verbose_name='PostalCode'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='telehpone',
            field=models.CharField(help_text='تلفن دفتر مرکزی', max_length=15, verbose_name='Telephone'),
        ),
    ]

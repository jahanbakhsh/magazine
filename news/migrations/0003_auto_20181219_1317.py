# Generated by Django 2.1.4 on 2018-12-19 13:17

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20181219_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
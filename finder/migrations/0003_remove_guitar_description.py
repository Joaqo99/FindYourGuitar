# Generated by Django 3.2.4 on 2021-08-26 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0002_auto_20210825_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guitar',
            name='description',
        ),
    ]

# Generated by Django 3.2.4 on 2021-09-13 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0009_alter_guitar_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_name', models.CharField(max_length=50, null=True)),
                ('status_id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]

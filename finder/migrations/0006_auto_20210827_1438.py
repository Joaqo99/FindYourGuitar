# Generated by Django 3.2.4 on 2021-08-27 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0005_guitar_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='guitar',
            name='search',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finder.search'),
        ),
    ]
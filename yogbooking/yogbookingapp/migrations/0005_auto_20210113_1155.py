# Generated by Django 3.0.7 on 2021-01-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yogbookingapp', '0004_booking_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_of_event',
            field=models.DateField(blank=True, default='none', null=True),
        ),
    ]

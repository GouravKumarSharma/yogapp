# Generated by Django 3.0.7 on 2021-01-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20210115_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]

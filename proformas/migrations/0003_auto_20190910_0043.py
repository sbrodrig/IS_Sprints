# Generated by Django 2.2.4 on 2019-09-10 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proformas', '0002_auto_20190910_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proforma',
            name='anexos',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

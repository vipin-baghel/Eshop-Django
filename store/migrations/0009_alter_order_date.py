# Generated by Django 4.0.6 on 2022-07-30 20:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 7, 31, 2, 18, 30, 409949)),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-31 08:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_order_amount_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 7, 31, 8, 21, 42, 928285, tzinfo=utc)),
        ),
    ]

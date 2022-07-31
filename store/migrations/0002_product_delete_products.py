# Generated by Django 4.0.6 on 2022-07-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=1000)),
                ('image', models.ImageField(upload_to='uploads/products_img/')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
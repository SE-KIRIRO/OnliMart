# Generated by Django 4.1.13 on 2023-12-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
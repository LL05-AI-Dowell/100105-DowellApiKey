# Generated by Django 4.2.2 on 2023-06-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_voucher_voucher_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='voucher_discount',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 3.1.1 on 2021-01-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0018_auto_20201228_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='phone',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]

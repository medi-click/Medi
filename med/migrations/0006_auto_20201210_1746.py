# Generated by Django 3.1.1 on 2020-12-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0005_product_manufacturered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
# Generated by Django 3.1.1 on 2020-12-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0004_auto_20201210_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufacturered_by',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
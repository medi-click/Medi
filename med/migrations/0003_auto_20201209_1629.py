# Generated by Django 3.1.1 on 2020-12-09 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0002_auto_20201209_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]

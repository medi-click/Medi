# Generated by Django 3.1.1 on 2020-12-24 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0013_auto_20201221_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='med.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='med.product')),
            ],
        ),
    ]

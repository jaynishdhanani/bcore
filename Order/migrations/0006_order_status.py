# Generated by Django 5.1 on 2024-10-16 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0005_rename_finaltotal_charge_order_order_finaltotal_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default=None, max_length=15),
        ),
    ]

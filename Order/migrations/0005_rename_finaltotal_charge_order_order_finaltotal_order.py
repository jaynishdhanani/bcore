# Generated by Django 5.1 on 2024-10-11 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_order_finaltotal_charge_order_order_subtotal_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='finaltotal_charge_order',
            new_name='finaltotal_order',
        ),
    ]

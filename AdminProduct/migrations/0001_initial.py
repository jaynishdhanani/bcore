# Generated by Django 5.1 on 2024-08-29 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_title', models.CharField(max_length=255)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_image', models.CharField(default='abc', max_length=100)),
                ('product_videourl', models.URLField(blank=True, max_length=255, null=True)),
                ('product_description', models.TextField()),
                ('product_specification', models.TextField()),
                ('product_isactive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_product',
            },
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_products_options_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_products_brand_products_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fleet_code', models.CharField(max_length=20, null=True)),
                ('plant_name', models.CharField(max_length=100, null=True)),
                ('mileage', models.PositiveBigIntegerField(null=True)),
                ('comments', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Plant',
            },
        ),
    ]
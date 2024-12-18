# Generated by Django 5.1.3 on 2024-11-13 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridge',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='FridgeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='fridge_images/')),
                ('fridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fridges.fridge')),
            ],
        ),
    ]

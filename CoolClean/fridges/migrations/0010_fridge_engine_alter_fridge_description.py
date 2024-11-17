# Generated by Django 5.1.3 on 2024-11-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridges', '0009_alter_fridge_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fridge',
            name='engine',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fridge',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-13 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridges', '0002_alter_fridge_price_fridgeimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='fridge',
            name='chamber_count',
            field=models.IntegerField(choices=[(1, '1 камера'), (2, '2 камеры'), (3, '3 камеры'), (4, '4 камеры')], default=1),
        ),
        migrations.AddField(
            model_name='fridge',
            name='color',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='fridge',
            name='defrosting_type',
            field=models.CharField(choices=[('no_frost', 'No Frost'), ('manual', 'Ручная'), ('without_freezer', 'Без морозильника')], default='manual', max_length=20),
        ),
        migrations.AddField(
            model_name='fridge',
            name='door_count',
            field=models.IntegerField(choices=[(1, '1 дверь'), (2, '2 двери'), (3, '3 двери'), (4, '4 двери'), (5, '5 дверей')], default=2),
        ),
        migrations.AddField(
            model_name='fridge',
            name='freezer_location',
            field=models.CharField(choices=[('top', 'сверху'), ('bottom', 'снизу'), ('left', 'слева'), ('right', 'справа'), ('no', 'нет')], default='top', max_length=20),
        ),
        migrations.AddField(
            model_name='fridge',
            name='height',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='fridge',
            name='width',
            field=models.FloatField(null=True),
        ),
    ]

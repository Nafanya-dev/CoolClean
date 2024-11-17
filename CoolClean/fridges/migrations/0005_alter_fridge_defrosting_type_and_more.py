# Generated by Django 5.1.3 on 2024-11-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridges', '0004_alter_fridge_defrosting_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridge',
            name='defrosting_type',
            field=models.CharField(choices=[('No Frost', 'No Frost'), ('ручная', 'Ручная'), ('Без морозильника', 'Без морозильника')], default='ручная', max_length=20),
        ),
        migrations.AlterField(
            model_name='fridge',
            name='freezer_location',
            field=models.CharField(choices=[('cверху', 'сверху'), ('снизу', 'снизу'), ('слева', 'слева'), ('справа', 'справа'), ('нет', 'нет')], default='сверху', max_length=20),
        ),
    ]

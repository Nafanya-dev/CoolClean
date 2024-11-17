from django.db import models


class Fridge(models.Model):
    DEFROSTING_CHOICES = [
        ('No Frost', 'No Frost'),
        ('Ручная', 'Ручная'),
        ('Без морозильника', 'Без морозильника'),
    ]

    CHAMBER_COUNT_CHOICES = [
        (1, '1 камера'),
        (2, '2 камеры'),
        (3, '3 камеры'),
        (4, '4 камеры'),
    ]

    FREEZER_LOCATION_CHOICES = [
        ('cверху', 'сверху'),
        ('снизу', 'снизу'),
        ('слева', 'слева'),
        ('справа', 'справа'),
        ('нет', 'нет'),
    ]

    DOOR_COUNT_CHOICES = [
        (1, '1 дверь'),
        (2, '2 двери'),
        (3, '3 двери'),
        (4, '4 двери'),
        (5, '5 дверей'),
    ]

    name = models.CharField(max_length=255,
                            default='Холодильник с морозильником')

    brand = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)
    height = models.CharField(max_length=10, null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    defrosting_type = models.CharField(max_length=20,
                                       choices=DEFROSTING_CHOICES,
                                       default='Ручная')

    freezer_location = models.CharField(max_length=20,
                                        choices=FREEZER_LOCATION_CHOICES,
                                        default='сверху')

    chamber_count = models.IntegerField(choices=CHAMBER_COUNT_CHOICES,
                                        default=1)

    door_count = models.IntegerField(choices=DOOR_COUNT_CHOICES,
                                     default=2)

    price = models.DecimalField(max_digits=10, decimal_places=0)
    engine = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.brand}, {self.color}'


class FridgeImage(models.Model):
    fridge = models.ForeignKey(Fridge, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fridge_images/')

    def __str__(self):
        return f"Image for {self.fridge.name}"

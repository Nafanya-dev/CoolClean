from django.db import models


class Washer(models.Model):
    LOAD_CHOICES = [
        ('Фронтальная', 'Фронтальная'),
        ('Вертикальная', 'Вертикальная'),
    ]

    name = models.CharField(max_length=255,
                            default='Стиральная машина')

    brand = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)
    height = models.CharField(max_length=10, null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    max_load = models.FloatField(null=True, blank=True)
    load_type = models.CharField(max_length=12, choices=LOAD_CHOICES,
                                 default='Фронтальная')

    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f'{self.name}, {self.brand}, {self.color}'


class WasherImage(models.Model):
    washer = models.ForeignKey(Washer, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='washer_images/')

    def __str__(self):
        return f"Image for {self.washer.name}"

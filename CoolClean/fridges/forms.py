from django import forms
from CoolClean.fridges.models import Fridge, FridgeImage


class FridgeForm(forms.ModelForm):
    class Meta:
        model = Fridge
        fields = ['name', 'brand', 'description', 'color', 'height',
                  'width', 'defrosting_type', 'freezer_location',
                  'chamber_count', 'door_count', 'price', 'engine']
        labels = {
            'name': 'Название:',
            'brand': 'Бренд:',
            'description': 'Описание:',
            'color': 'Цвет:',
            'price': 'Цена:',
            'height': 'Высота:',
            'width': 'Ширина:',
            'defrosting_type': 'Разморозка морозильной камеры:',
            'chamber_count': 'Количество камер:',
            'freezer_location': 'Расположение морозильника:',
            'door_count': 'Количество дверей:',
            'engine': 'Двигатель'
        }

    def __init__(self, *args, **kwargs):
        super(FridgeForm, self).__init__(*args, **kwargs)
        self.fields['defrosting_type'].widget.attrs['class'] = 'form-select'
        self.fields['chamber_count'].widget.attrs['class'] = 'form-select'
        self.fields['freezer_location'].widget.attrs['class'] = 'form-select'
        self.fields['door_count'].widget.attrs['class'] = 'form-select'

        for field in self.fields:
            if field not in ['defrosting_type', 'chamber_count',
                             'freezer_location', 'door_count']:
                self.fields[field].widget.attrs['class'] = 'form-control'


class FridgeImageForm(forms.ModelForm):
    class Meta:
        model = FridgeImage
        fields = ['image']

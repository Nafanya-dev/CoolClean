from django import forms
from CoolClean.washers.models import Washer, WasherImage


class WasherForm(forms.ModelForm):
    class Meta:
        model = Washer
        fields = ['name', 'brand', 'description', 'color', 'height',
                  'width', 'max_load', 'load_type', 'price']

        labels = {
            'name': 'Название:',
            'brand': 'Бренд:',
            'description': 'Описание:',
            'color': 'Цвет:',
            'price': 'Цена:',
            'height': 'Высота:',
            'width': 'Ширина:',
            'max_load': 'Максимальная загрузка',
            'load_type': 'Тип загрузки',
        }

    def __init__(self, *args, **kwargs):
        super(WasherForm, self).__init__(*args, **kwargs)
        self.fields['load_type'].widget.attrs['class'] = 'form-select'

        for field in self.fields:
            if field not in ['load_type']:
                self.fields[field].widget.attrs['class'] = 'form-control'


class WasherImageForm(forms.ModelForm):
    class Meta:
        model = WasherImage
        fields = ['image']

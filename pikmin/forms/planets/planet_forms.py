from django import forms

from pikmin.models.planets.planet import Planet


class PlanetSearchForm(forms.Form):

    name = forms.CharField(
        label='惑星名',
        max_length=40,
        required=False,
    )

    name_kana = forms.CharField(
        label='惑星名カナ',
        max_length=80,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(PlanetSearchForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class PlanetForm(forms.ModelForm):

    class Meta:
        model = Planet
        fields = (
            'name',
            'name_kana',
        )

    def __init__(self, *args, **kwargs):
        super(PlanetForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
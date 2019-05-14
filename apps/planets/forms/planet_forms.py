from django import forms

from apps.planets.models.planet import Planet
from apps.planets.models.onion import Onion


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
        model = Onion
        fields = (
            'name',
            'started_on',
            'ended_on',
        )

    def __init__(self, *args, **kwargs):
        super(PlanetForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


OnionFormset = forms.inlineformset_factory(
    Planet,
    Onion,
    PlanetForm,
    extra=1,
    can_delete=True,
)
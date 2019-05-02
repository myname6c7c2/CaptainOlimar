from django import forms

from pikmin.models.pikmins.pikmin import Pikmin
from pikmin.lib.choices import SEX


class PikminSearchForm(forms.Form):

    last_name = forms.CharField(
        label='苗字',
        max_length=20,
        required=False,
    )

    first_name = forms.CharField(
        label='名前',
        max_length=20,
        required=False,
    )

    last_name_kana = forms.CharField(
        label='苗字カナ',
        max_length=40,
        required=False,
    )

    first_name_kana = forms.CharField(
        label='名前カナ',
        max_length=40,
        required=False,
    )

    sex = forms.ChoiceField(
        label='性別',
        choices=SEX,
    )

    def __init__(self, *args, **kwargs):
        super(PikminSearchForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
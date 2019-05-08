from datetime import date

from django.db import models
from django.db.models import Q
from django.utils import timezone

from apps.lib.choices import SEX


class Pikmin(models.Model):

    first_name = models.CharField('名前', max_length=20)
    last_name = models.CharField('苗字', max_length=20)
    first_name_kana = models.CharField('名前カナ', max_length=40, blank=True, null=True)
    last_name_kana = models.CharField('苗字カナ', max_length=40, blank=True, null=True)
    birth_date = models.DateField('生年月日', default=timezone.now)
    sex = models.IntegerField('性別', choices=SEX)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.last_name + self.first_name

    @property
    def calculate_age(self):
        today = date.today()
        delta = today - self.birth_date
        age = 0
        total_day = delta.days
        for year in range(self.birth_date.year, today.year):
            is_leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
            if is_leap_year:
                day = 366
            else:
                day = 365

            if  total_day >= day:
                age += 1
                total_day -= day

        return age

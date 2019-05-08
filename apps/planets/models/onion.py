from django.db import models

from apps.planets.models.planet import Planet


class Onion(models.Model):

    name = models.CharField('オニオン名', max_length=40)
    started_on = models.DateField('開始日')
    ended_on = models.DateField('終了日', blank=True, null=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='惑星')

    def __str__(self):
        return self.name
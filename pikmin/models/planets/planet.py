from django.db import models


class Planet(models.Model):

    name = models.CharField('惑星名', max_length=40)
    name_kana = models.CharField('惑星名カナ', max_length=80, blank=True, null=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.name
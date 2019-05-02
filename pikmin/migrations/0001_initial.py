# Generated by Django 2.2 on 2019-04-28 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pikmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='名前')),
                ('last_name', models.CharField(max_length=20, verbose_name='苗字')),
                ('first_name_kana', models.CharField(blank=True, max_length=40, null=True, verbose_name='名前カナ')),
                ('last_name_kana', models.CharField(blank=True, max_length=40, null=True, verbose_name='苗字カナ')),
                ('birth_date', models.DateField(default=django.utils.timezone.now, verbose_name='生年月日')),
                ('sex', models.IntegerField(choices=[(0, ''), (1, '男'), (2, '女')], verbose_name='性別')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
    ]
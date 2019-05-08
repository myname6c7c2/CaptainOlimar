# Generated by Django 2.2 on 2019-05-08 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='惑星名')),
                ('name_kana', models.CharField(blank=True, max_length=80, null=True, verbose_name='惑星名カナ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
        migrations.CreateModel(
            name='Onion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='オニオン名')),
                ('started_on', models.DateField(verbose_name='開始日')),
                ('ended_on', models.DateField(blank=True, null=True, verbose_name='終了日')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planets.Planet', verbose_name='惑星')),
            ],
        ),
    ]
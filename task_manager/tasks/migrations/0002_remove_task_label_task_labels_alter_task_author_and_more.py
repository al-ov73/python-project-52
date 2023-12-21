# Generated by Django 5.0 on 2023-12-21 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('statuses', '0001_initial'),
        ('tasks', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='label',
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, to='labels.label', verbose_name='Метки'),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to='users.profile', verbose_name='Только свои задачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='task',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsible', to='users.profile', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.status', verbose_name='Статус'),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-11 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_team_advisor_team_advisor_en_team_advisor_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='summary',
            field=models.TextField(max_length=500, null=True, verbose_name='summary'),
        ),
        migrations.AddField(
            model_name='team',
            name='summary_en',
            field=models.TextField(max_length=500, null=True, verbose_name='summary'),
        ),
        migrations.AddField(
            model_name='team',
            name='summary_ru',
            field=models.TextField(max_length=500, null=True, verbose_name='summary'),
        ),
        migrations.AddField(
            model_name='team',
            name='summary_uz',
            field=models.TextField(max_length=500, null=True, verbose_name='summary'),
        ),
        migrations.AlterField(
            model_name='team',
            name='title',
            field=models.CharField(max_length=250, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='team',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='team',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='team',
            name='title_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='title'),
        ),
    ]

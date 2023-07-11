# Generated by Django 4.2.3 on 2023-07-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_team_summary_team_summary_en_team_summary_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='detail_title',
            field=models.CharField(max_length=250, null=True, verbose_name='detail_title'),
        ),
        migrations.AddField(
            model_name='team',
            name='detail_title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='detail_title'),
        ),
        migrations.AddField(
            model_name='team',
            name='detail_title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='detail_title'),
        ),
        migrations.AddField(
            model_name='team',
            name='detail_title_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='detail_title'),
        ),
        migrations.AlterField(
            model_name='team',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='team',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='team',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='team',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
    ]
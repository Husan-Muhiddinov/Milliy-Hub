# Generated by Django 4.2.3 on 2023-07-11 05:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_addvertising_alter_services_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='advisor',
            field=models.CharField(max_length=70, null=True, verbose_name='advisor'),
        ),
        migrations.AddField(
            model_name='team',
            name='advisor_en',
            field=models.CharField(max_length=70, null=True, verbose_name='advisor'),
        ),
        migrations.AddField(
            model_name='team',
            name='advisor_ru',
            field=models.CharField(max_length=70, null=True, verbose_name='advisor'),
        ),
        migrations.AddField(
            model_name='team',
            name='advisor_uz',
            field=models.CharField(max_length=70, null=True, verbose_name='advisor'),
        ),
        migrations.AddField(
            model_name='team',
            name='body',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='team',
            name='body_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='team',
            name='body_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='team',
            name='body_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='team',
            name='client_name',
            field=models.CharField(max_length=70, null=True, verbose_name='client_name'),
        ),
        migrations.AddField(
            model_name='team',
            name='client_name_en',
            field=models.CharField(max_length=70, null=True, verbose_name='client_name'),
        ),
        migrations.AddField(
            model_name='team',
            name='client_name_ru',
            field=models.CharField(max_length=70, null=True, verbose_name='client_name'),
        ),
        migrations.AddField(
            model_name='team',
            name='client_name_uz',
            field=models.CharField(max_length=70, null=True, verbose_name='client_name'),
        ),
        migrations.AddField(
            model_name='team',
            name='location',
            field=models.CharField(max_length=70, null=True, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='team',
            name='location_en',
            field=models.CharField(max_length=70, null=True, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='team',
            name='location_ru',
            field=models.CharField(max_length=70, null=True, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='team',
            name='location_uz',
            field=models.CharField(max_length=70, null=True, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='team',
            name='project_under',
            field=models.CharField(max_length=70, null=True, verbose_name='project_under'),
        ),
        migrations.AddField(
            model_name='team',
            name='project_under_en',
            field=models.CharField(max_length=70, null=True, verbose_name='project_under'),
        ),
        migrations.AddField(
            model_name='team',
            name='project_under_ru',
            field=models.CharField(max_length=70, null=True, verbose_name='project_under'),
        ),
        migrations.AddField(
            model_name='team',
            name='project_under_uz',
            field=models.CharField(max_length=70, null=True, verbose_name='project_under'),
        ),
        migrations.AddField(
            model_name='team',
            name='project_value',
            field=models.DecimalField(decimal_places=2, max_digits=70, null=True, verbose_name='project_value'),
        ),
        migrations.AddField(
            model_name='team',
            name='status',
            field=models.CharField(choices=[('akseleratsiya', 'akseleratsiya'), ('inkubatsiya', 'inkubatsiya')], max_length=100, null=True, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='team',
            name='year_completed',
            field=models.IntegerField(null=True, verbose_name='year_completed'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-12 01:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_team_detail_title_team_detail_title_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit_Assuranse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('body_en', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
                ('body_ru', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
                ('body_uz', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
            ],
        ),
        migrations.CreateModel(
            name='Finansial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('body_en', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
                ('body_ru', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
                ('body_uz', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
            ],
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('body_en', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
                ('body_ru', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
                ('body_uz', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
            ],
        ),
        migrations.CreateModel(
            name='Strategic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('body_en', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
                ('body_ru', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
                ('body_uz', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
            ],
        ),
        migrations.CreateModel(
            name='Trade_Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('body_en', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
                ('body_ru', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
                ('body_uz', ckeditor.fields.RichTextField(null=True, verbose_name='body')),
            ],
        ),
        migrations.AlterField(
            model_name='team',
            name='summary',
            field=models.TextField(null=True, verbose_name='summary'),
        ),
        migrations.AlterField(
            model_name='team',
            name='summary_en',
            field=models.TextField(null=True, verbose_name='summary'),
        ),
        migrations.AlterField(
            model_name='team',
            name='summary_ru',
            field=models.TextField(null=True, verbose_name='summary'),
        ),
        migrations.AlterField(
            model_name='team',
            name='summary_uz',
            field=models.TextField(null=True, verbose_name='summary'),
        ),
    ]

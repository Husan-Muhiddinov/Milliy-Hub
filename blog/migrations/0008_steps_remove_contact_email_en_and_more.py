# Generated by Django 4.2.3 on 2023-07-07 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_contact_telegram_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('title_en', models.CharField(max_length=30, null=True)),
                ('title_ru', models.CharField(max_length=30, null=True)),
                ('title_uz', models.CharField(max_length=30, null=True)),
                ('body', models.CharField(max_length=100)),
                ('body_en', models.CharField(max_length=100, null=True)),
                ('body_ru', models.CharField(max_length=100, null=True)),
                ('body_uz', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email_en',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email_ru',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email_uz',
        ),
    ]

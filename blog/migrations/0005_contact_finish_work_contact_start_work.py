# Generated by Django 4.2.3 on 2023-07-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='finish_work',
            field=models.CharField(max_length=10, null=True, verbose_name='finish_work'),
        ),
        migrations.AddField(
            model_name='contact',
            name='start_work',
            field=models.CharField(max_length=10, null=True, verbose_name='start_work'),
        ),
    ]

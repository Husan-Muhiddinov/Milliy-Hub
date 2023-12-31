# Generated by Django 4.2.3 on 2023-07-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_contact_link1_remove_contact_link2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=50, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='facebook_link',
            field=models.CharField(max_length=30, null=True, verbose_name='facebook_link'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='instagram_link',
            field=models.CharField(max_length=30, null=True, verbose_name='instagram_link'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='linkedin_link',
            field=models.CharField(max_length=30, null=True, verbose_name='linkedin_link'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(null=True, verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telegram_link',
            field=models.CharField(max_length=30, null=True, verbose_name='telegram_link'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='twitter_link',
            field=models.CharField(max_length=30, null=True, verbose_name='twitter_link'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='work_created_at',
            field=models.TimeField(null=True, verbose_name='work_created_at'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='work_updated_at',
            field=models.TimeField(null=True, verbose_name='work_updated_at'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='youtube_link',
            field=models.CharField(max_length=30, null=True, verbose_name='youtube_link'),
        ),
    ]

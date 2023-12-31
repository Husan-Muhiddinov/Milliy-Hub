# Generated by Django 4.2.3 on 2023-07-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_card_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='title_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='title_uz',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

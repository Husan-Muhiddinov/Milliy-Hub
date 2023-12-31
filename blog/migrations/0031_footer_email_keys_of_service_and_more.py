# Generated by Django 4.2.3 on 2023-07-14 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_departmentcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer_Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Keys_of_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benifits', models.TextField(null=True, verbose_name='benifits')),
                ('benifits_en', models.TextField(null=True, verbose_name='benifits')),
                ('benifits_ru', models.TextField(null=True, verbose_name='benifits')),
                ('benifits_uz', models.TextField(null=True, verbose_name='benifits')),
                ('mutual_funds', models.TextField(null=True, verbose_name='mutual_funds')),
                ('mutual_funds_en', models.TextField(null=True, verbose_name='mutual_funds')),
                ('mutual_funds_ru', models.TextField(null=True, verbose_name='mutual_funds')),
                ('mutual_funds_uz', models.TextField(null=True, verbose_name='mutual_funds')),
                ('company_growth', models.TextField(null=True, verbose_name='company_growth')),
                ('company_growth_en', models.TextField(null=True, verbose_name='company_growth')),
                ('company_growth_ru', models.TextField(null=True, verbose_name='company_growth')),
                ('company_growth_uz', models.TextField(null=True, verbose_name='company_growth')),
            ],
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='benifits',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='benifits_en',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='benifits_ru',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='benifits_uz',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='company_growth',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='company_growth_en',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='company_growth_ru',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='company_growth_uz',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='mutual_funds',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='mutual_funds_en',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='mutual_funds_ru',
        ),
        migrations.RemoveField(
            model_name='our_keys_of_service',
            name='mutual_funds_uz',
        ),
    ]

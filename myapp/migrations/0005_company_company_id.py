# Generated by Django 4.0.6 on 2023-02-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_company_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_id',
            field=models.CharField(max_length=50, null=True, verbose_name='company_id'),
        ),
    ]

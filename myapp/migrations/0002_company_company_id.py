# Generated by Django 4.0.6 on 2023-02-15 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='company_name'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-14 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_models_from_csv', '0004_auto_20190601_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicmodel',
            name='csv_google_sheets_auth_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
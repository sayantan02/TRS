# Generated by Django 4.1.2 on 2022-11-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_registrationnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes'),
        ),
    ]
# Generated by Django 3.2.16 on 2022-11-09 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=20)),
                ('guardian_name', models.CharField(max_length=50)),
                ('guardian_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('admission_date', models.DateField(auto_now_add=True)),
                ('admission_fees', models.IntegerField()),
                ('payment_mode', models.IntegerField()),
                ('status', models.IntegerField()),
                ('picture', models.ImageField(upload_to='students')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.course')),
            ],
        ),
    ]
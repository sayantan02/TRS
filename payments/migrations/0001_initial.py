# Generated by Django 4.1.2 on 2022-11-12 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0007_registrationnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(blank=True, max_length=120, null=True)),
                ('payment_amount', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.student')),
            ],
            options={
                'ordering': ('-datetime',),
            },
        ),
    ]

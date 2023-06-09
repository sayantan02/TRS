# Generated by Django 4.1.3 on 2022-11-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_student_guardian_number_batch_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_fees',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='payment_mode',
            field=models.CharField(choices=[('CASH', 'Cash'), ('ONLINE', 'Online')], default='ACTIVE', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'InActive')], default='ONLINE', max_length=30),
        ),
    ]

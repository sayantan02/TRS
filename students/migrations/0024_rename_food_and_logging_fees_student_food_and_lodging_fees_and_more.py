# Generated by Django 4.1.2 on 2022-12-06 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0023_student_belt_fees_student_cap_fees_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='food_and_logging_fees',
            new_name='food_and_lodging_fees',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_of_admission',
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_batch_admission_fees_batch_book_fees_batch_bp_fees_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='guardian_number',
        ),
        migrations.AddField(
            model_name='batch',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='guardian_mobile_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_fees',
            field=models.CharField(choices=[('COOCHBEHAR', 'Cooch Behar'), ('ALIPURDUAR', 'Alipurduar')], default='ONLINE', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='payment_mode',
            field=models.CharField(choices=[('COOCHBEHAR', 'Cooch Behar'), ('ALIPURDUAR', 'Alipurduar')], default='ACTIVE', max_length=30),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artish_freelancers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='hourly_rate_max',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='hourly_rate_min',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]

# Generated by Django 5.1.1 on 2024-12-16 16:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_alter_contract_attraction_bonus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='base_salary',
            field=models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(10000000)], verbose_name='حقوق پایه'),
        ),
    ]

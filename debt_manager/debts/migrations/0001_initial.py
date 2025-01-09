# Generated by Django 5.1.4 on 2025-01-09 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_amount', models.FloatField()),
                ('interest_rate', models.FloatField()),
                ('minimum_payment', models.FloatField()),
                ('due_date', models.DateField()),
            ],
        ),
    ]

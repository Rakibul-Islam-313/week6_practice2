# Generated by Django 4.2.7 on 2024-01-03 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MoneyTransfer',
        ),
    ]

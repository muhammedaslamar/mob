# Generated by Django 2.2 on 2021-09-06 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_reg_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='reg',
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-23 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_updated',
        ),
    ]
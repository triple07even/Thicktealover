# Generated by Django 3.0.5 on 2020-09-22 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0060_profile_email_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='socials',
            name='facebook',
        ),
    ]

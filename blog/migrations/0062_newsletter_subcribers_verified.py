# Generated by Django 3.0.5 on 2020-09-22 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0061_auto_20200922_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter_subcribers',
            name='verified',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
# Generated by Django 3.0.5 on 2020-08-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20200823_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_flag',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

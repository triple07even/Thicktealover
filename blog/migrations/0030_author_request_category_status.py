# Generated by Django 3.0.5 on 2020-08-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20200820_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='author_request_category',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
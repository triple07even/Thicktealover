# Generated by Django 3.0.5 on 2020-08-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_author_request_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author_request',
            name='message',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='author_request',
            name='title',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='author_request_category',
            name='category',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='author_request_category',
            name='options',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
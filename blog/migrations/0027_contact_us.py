# Generated by Django 3.0.5 on 2020-08-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_author_request_markas_read'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, null=True)),
                ('last_name', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=20, null=True)),
                ('phone_number', models.IntegerField(max_length=20, null=True)),
                ('messages', models.CharField(max_length=70, null=True)),
            ],
        ),
    ]
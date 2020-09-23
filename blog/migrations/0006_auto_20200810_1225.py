# Generated by Django 3.0.5 on 2020-08-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200810_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(default='IMG_20200503_094546.jpg', null=True, upload_to='profile/images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
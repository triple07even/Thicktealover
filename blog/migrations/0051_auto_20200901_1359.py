# Generated by Django 3.0.5 on 2020-09-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0050_post_number_of_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_voice',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(default='big_img_1.jpg', upload_to='images/'),
        ),
    ]
# Generated by Django 3.0.5 on 2020-09-07 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0057_comment_active_writer_inst'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='co_author_voice',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
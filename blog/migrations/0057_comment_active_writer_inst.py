# Generated by Django 3.0.5 on 2020-09-07 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0056_auto_20200907_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active_writer_inst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

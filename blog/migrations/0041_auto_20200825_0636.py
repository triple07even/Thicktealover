# Generated by Django 3.0.5 on 2020-08-25 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_auto_20200825_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaburating_author',
            name='approved_on',
            field=models.DateField(null=True),
        ),
    ]
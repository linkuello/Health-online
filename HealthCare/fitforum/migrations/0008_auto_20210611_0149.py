# Generated by Django 3.1.7 on 2021-06-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitforum', '0007_auto_20210610_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]

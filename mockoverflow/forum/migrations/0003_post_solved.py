# Generated by Django 3.0.7 on 2020-07-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200710_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='solved',
            field=models.BooleanField(default=False),
        ),
    ]

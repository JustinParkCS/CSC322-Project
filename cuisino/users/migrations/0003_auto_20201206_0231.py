# Generated by Django 3.1.2 on 2020-12-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201206_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='complain',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customers',
            name='compliment',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employees',
            name='complain',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employees',
            name='compliment',
            field=models.SmallIntegerField(default=0),
        ),
    ]
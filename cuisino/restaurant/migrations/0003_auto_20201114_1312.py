# Generated by Django 3.1.2 on 2020-11-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20201111_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='itemReviews',
            field=models.TextField(blank=True, null=True),
        ),
    ]

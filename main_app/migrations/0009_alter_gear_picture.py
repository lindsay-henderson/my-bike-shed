# Generated by Django 4.1.3 on 2022-11-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_bike_gear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='picture',
            field=models.CharField(default='paste link to an image of item ', max_length=200),
        ),
    ]
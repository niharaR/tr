# Generated by Django 4.1.5 on 2023-03-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='desc',
            field=models.TextField(default='e'),
            preserve_default=False,
        ),
    ]

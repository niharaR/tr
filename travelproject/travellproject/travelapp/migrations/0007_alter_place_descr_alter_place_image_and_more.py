# Generated by Django 4.1.5 on 2023-03-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0006_delete_picture_place_descr_place_image_place_namee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='descr',
            field=models.TextField(default='he1'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(default='path/to/image.png', upload_to='pt'),
        ),
        migrations.AlterField(
            model_name='place',
            name='namee',
            field=models.CharField(default='dd', max_length=150),
        ),
    ]

# Generated by Django 4.2 on 2023-04-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_pieces', '0002_artpiece_image_alter_artpiece_date_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artpiece',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]

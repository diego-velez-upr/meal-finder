# Generated by Django 4.1.6 on 2023-04-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_food__tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        )
    ]

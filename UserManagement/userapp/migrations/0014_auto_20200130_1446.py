# Generated by Django 2.2.2 on 2020-01-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_auto_20200130_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

# Generated by Django 2.2.2 on 2020-01-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_auto_20200130_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
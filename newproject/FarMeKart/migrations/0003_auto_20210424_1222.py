# Generated by Django 3.0 on 2021-04-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarMeKart', '0002_auto_20210424_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extpro',
            name='impf',
            field=models.ImageField(default='farmerlogo.png', upload_to='pro/'),
        ),
        migrations.AlterField(
            model_name='vegpro',
            name='impf',
            field=models.ImageField(default='user logo.png', upload_to='images/'),
        ),
    ]

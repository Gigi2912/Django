# Generated by Django 2.2.3 on 2019-07-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

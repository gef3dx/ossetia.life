# Generated by Django 4.0 on 2022-01-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_navbar_options_navbar_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='position',
            field=models.IntegerField(default=0, max_length=50, verbose_name='Позиция'),
        ),
    ]

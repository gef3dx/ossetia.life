# Generated by Django 4.0 on 2022-01-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_navbar_alter_category_slug_alter_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='navbar',
            options={'verbose_name': 'Меню сайта', 'verbose_name_plural': 'Элементы меню'},
        ),
        migrations.AddField(
            model_name='navbar',
            name='posted',
            field=models.BooleanField(default=False, verbose_name='Опубликованно'),
        ),
    ]
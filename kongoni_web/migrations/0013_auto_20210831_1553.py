# Generated by Django 3.1.7 on 2021-08-31 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kongoni_web', '0012_auto_20210816_1246'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tourism',
            new_name='Farm',
        ),
        migrations.RenameModel(
            old_name='Trend',
            new_name='News',
        ),
        migrations.RenameModel(
            old_name='Lake',
            new_name='Office',
        ),
        migrations.RenameModel(
            old_name='Station',
            new_name='Travel',
        ),
        migrations.AlterModelTable(
            name='farm',
            table='Agriculture',
        ),
        migrations.AlterModelTable(
            name='news',
            table='News',
        ),
        migrations.AlterModelTable(
            name='office',
            table='Offices',
        ),
        migrations.AlterModelTable(
            name='travel',
            table='Travel',
        ),
    ]

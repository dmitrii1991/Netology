# Generated by Django 2.2.4 on 2019-10-03 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0014_оrder_total_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='оrder',
            old_name='сat',
            new_name='сart',
        ),
    ]
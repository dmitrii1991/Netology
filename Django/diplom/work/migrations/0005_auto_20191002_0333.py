# Generated by Django 2.2.4 on 2019-10-02 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20191002_0328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='сategory_bd',
        ),
        migrations.AddField(
            model_name='bd',
            name='сategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.Category'),
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-18 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('system', models.CharField(max_length=50)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('memory', models.IntegerField()),
                ('screen_resolution', models.IntegerField()),
                ('double_camera', models.BooleanField()),
                ('screen_size', models.CharField(max_length=50)),
                ('radio', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stylus', models.BooleanField()),
                ('double_screen', models.BooleanField()),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Nokia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_keyboard', models.BooleanField()),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Iphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_id', models.BooleanField()),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
    ]

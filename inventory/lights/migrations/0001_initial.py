# Generated by Django 2.2.1 on 2019-05-15 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light_type', models.CharField(max_length=100)),
                ('in_stock', models.IntegerField()),
                ('on_order', models.IntegerField()),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='LightLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lights.Light')),
            ],
        ),
    ]

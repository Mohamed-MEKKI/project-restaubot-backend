# Generated by Django 4.2.20 on 2025-03-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restaurants',
            fields=[
                ('restaurant_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
                ('phone', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('hours', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('reviews', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('categories', models.CharField(max_length=200)),
            ],
        ),
    ]

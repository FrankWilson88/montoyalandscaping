# Generated by Django 3.2.9 on 2021-11-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hardscape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='img/hardscape/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Hardscape',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Mowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='img/mowing/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Mowing',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Mulch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='img/mulch/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Mulching',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Powerwash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='img/powerwash/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Power Washing',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Stone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='img/stone/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Stone Install',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='img/tree/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tree Removal',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Trimming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='img/trimming/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Trimming',
                'ordering': ['timestamp'],
            },
        ),
    ]

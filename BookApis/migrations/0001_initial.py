# Generated by Django 5.0.4 on 2024-04-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('no_of_pages', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('publisher_name', models.CharField(max_length=100)),
            ],
        ),
    ]

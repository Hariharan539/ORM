# Generated by Django 5.2 on 2025-04-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Phone_Number', models.IntegerField()),
                ('MovieName', models.CharField(max_length=100)),
                ('seats', models.IntegerField()),
            ],
        ),
    ]

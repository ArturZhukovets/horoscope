# Generated by Django 4.0.3 on 2022-04-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horoscope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zodiac_name', models.CharField(max_length=30)),
                ('horoscope_description', models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('discount', models.FloatField()),
            ],
        ),
    ]

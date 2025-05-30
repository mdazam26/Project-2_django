# Generated by Django 5.2 on 2025-04-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurent_name', models.CharField(max_length=20)),
                ('picture_url', models.CharField(default='https://tse2.mm.bing.net/th/id/OIP.3JuA0-BIEyyCceG24Arr3gHaE8?rs=1&pid=ImgDetMain', max_length=200)),
                ('cuisine', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
            ],
        ),
    ]

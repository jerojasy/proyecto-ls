# Generated by Django 3.0 on 2020-06-11 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200611_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
    ]

# Generated by Django 3.0 on 2020-06-12 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200611_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomproducto', models.CharField(max_length=100)),
                ('SKU', models.CharField(blank=True, max_length=100, null=True)),
                ('marca', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True)),
                ('vencimiento', models.DateField()),
                ('preciocompra', models.IntegerField()),
                ('precioventa', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('stockcritico', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
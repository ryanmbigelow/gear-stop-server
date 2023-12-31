# Generated by Django 4.1.3 on 2023-07-29 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gearstopapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gearstopapi.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gearstopapi.product')),
            ],
        ),
    ]

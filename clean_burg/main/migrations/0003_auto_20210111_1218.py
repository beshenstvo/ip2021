# Generated by Django 3.0.11 on 2021-01-11 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210111_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='services',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.Order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='main.Service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Элемент заказа',
                'verbose_name_plural': 'Элементы заказа',
                'ordering': ('pk',),
            },
        ),
    ]

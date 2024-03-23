# Generated by Django 3.2.25 on 2024-03-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_delivery',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_option',
            field=models.CharField(choices=[('delivery', 'Delivery'), ('collection', 'Collection')], default='delivery', max_length=10),
        ),
    ]

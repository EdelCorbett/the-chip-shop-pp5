# Generated by Django 3.2.25 on 2024-04-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inquiry',
            options={'verbose_name_plural': 'Inquiries'},
        ),
        migrations.AddField(
            model_name='inquiry',
            name='contacted',
            field=models.BooleanField(default=False),
        ),
    ]
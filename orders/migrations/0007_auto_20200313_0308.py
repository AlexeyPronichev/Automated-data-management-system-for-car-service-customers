# Generated by Django 3.0.3 on 2020-03-13 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200313_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='message',
            field=models.TextField(max_length=250),
        ),
    ]

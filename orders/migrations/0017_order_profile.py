# Generated by Django 3.0.3 on 2020-03-14 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200313_0135'),
        ('orders', '0016_remove_order_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to='account.Profile'),
        ),
    ]

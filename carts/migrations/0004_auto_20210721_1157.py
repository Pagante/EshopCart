# Generated by Django 3.0 on 2021-07-21 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20210718_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.Cart'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_alter_iteminorder_count_alter_product_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
    ]

# Generated by Django 4.2.18 on 2025-02-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pic',
            field=models.ImageField(default='default-picture.png', upload_to='customers'),
        ),
    ]

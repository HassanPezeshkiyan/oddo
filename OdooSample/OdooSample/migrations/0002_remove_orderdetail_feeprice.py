# Generated by Django 5.0.6 on 2024-07-01 14:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("OdooSample", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderdetail",
            name="FeePrice",
        ),
    ]

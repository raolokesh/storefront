# Generated by Django 4.2.1 on 2023-07-06 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_product_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="inventary", new_name="inventory",
        ),
    ]
# Generated by Django 5.0 on 2024-05-31 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0002_contact_remove_product_product_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='comopsition',
            new_name='composition',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='product/default_image.jpg', upload_to='product'),
        ),
    ]

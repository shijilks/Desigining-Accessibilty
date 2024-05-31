# Generated by Django 5.0 on 2024-05-31 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='Product_image',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('GH', 'Ghee'), ('PA', 'Paneer'), ('CH', 'Cheese'), ('IC', 'Ice cream')], max_length=2),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='default_image_path.jpg', upload_to='product'),
            preserve_default=False,
        ),
    ]

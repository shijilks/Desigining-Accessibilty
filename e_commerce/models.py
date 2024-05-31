from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATE_CHOICES=(
    ('kerala','kerala'),
     ('Goa','Goa'),
      ('Delhi','Delhi'),
       ('Gujart','Gujart'),
       ('Tamil Nadu','Tamil Nadu'),
        ('Mumbi','Mumbi'),
        ('kolakatta','Kolatta'),
        ('Pune','Pune'),
)
CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('GH', 'Ghee'),
    ('PA', 'Paneer'),
    ('CH', 'Cheese'),
    ('IC', 'Ice cream'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default="")
    prodapp = models.TextField(default="")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product', default='product/default_image.jpg')  # Default image path

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality= models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile=models.IntegerField(default="")
    zipcode =models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Awaiting Approval"), (1, "Approved"))
CONDITION = ((0, "New"), (1, "Used"), (2, "Refurbished"))

# Create your models here.
class Product(models.Model):
    """
    Stores a single product entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_posts')
    product_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    condition = models.IntegerField(choices=CONDITION, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product: {self.title} | added by {self.author}"

    class Meta:
        ordering = ['-created_on', 'author']


class Basket(models.Model):
    """
    Stores a single basket entry related to :model:`auth.User` and :model:`products.Product`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Basket: {self.product} | added by {self.user}"

    class Meta:
        ordering = ['-created_on', 'user']
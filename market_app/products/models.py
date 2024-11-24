import uuid
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Категории 3д моделей.
    """
    name = models.CharField(max_length=20, 
                            unique=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Карточка 3д модели.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, 
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to='products/%Y/%m/%d',
                               blank=True)
    files = models.FileField(blank=True)
    category = models.ForeignKey(Category, 
                                 related_name='products', 
                                 on_delete=models.CASCADE)
    tags = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.DecimalField(default=0.000, 
                                   max_digits=4, 
                                   decimal_places=2)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("products:model_detail", 
                       args=['self.pk'])
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
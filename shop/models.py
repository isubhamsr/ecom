from django.db import models
import smtplib

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_desc = models.TextField()
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    price = models.IntegerField()
    publish_date = models.DateField()
    product_image = models.ImageField(upload_to='shop/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_id} - {self.product_name}"

class Order(models.Model):
    STATUS_CHOICES = (
    ('active','ACTIVE'),
    ('shipped', 'SHIPPED'),
    ('deliver','DELIVER'),
    )
    order_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    total_price = models.CharField(max_length=255, default="")
    date = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='active')
    ordered_item = models.TextField()

    def __str__(self):
        return f"{self.order_id} - {self.first_name}"

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    status = models.CharField(max_length=255, default="")
    update_desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_id} - {self.status}"

class ContactUs(models.Model):
    contact_id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.contact_id} - {self.name}"
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    Name = models.CharField(max_length=20)
    Image = models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return self.Name


class Customer(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.FirstName


class Bime(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Price = models.IntegerField(default=0)
    Offer = models.BooleanField(default=False)
    OfferPrice = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class Color(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    HexColor = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.Name

class Color2(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    HexColor = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.Name

class Color3(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    HexColor = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.Name
class Color4(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    HexColor = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.Name
class Color5(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    HexColor = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.Name


class Garanti(models.Model):
    Name = models.CharField(max_length=20, blank=True)
    Month = models.IntegerField(default=1)

    def __str__(self):
        return self.Name


class Owner_Product(models.Model):
    Name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=100)
    En_Name = models.CharField(max_length=100, null=True, blank=True)
    discription = models.CharField(max_length=200, default='', blank=True, null=True)
    City = models.CharField(max_length=30, null=True, blank=True)
    Price = models.IntegerField(default=0)
    Category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    Color = models.ForeignKey(Color, default=1, on_delete=models.CASCADE, null=True, blank=True)
    Color2 = models.ForeignKey(Color2, default=1, on_delete=models.CASCADE, null=True, blank=True)
    Color3 = models.ForeignKey(Color3, default=1, on_delete=models.CASCADE, null=True, blank=True)
    Color4 = models.ForeignKey(Color4, default=1, on_delete=models.CASCADE, null=True, blank=True)
    Color5 = models.ForeignKey(Color5, default=1, on_delete=models.CASCADE, null=True, blank=True)
    send = models.BooleanField(default=False)
    Send_Price = models.IntegerField(default=0, null=True, blank=True )
    Garanti = models.ForeignKey(Garanti, default=1, null=True, on_delete=models.CASCADE)
    Bime = models.ForeignKey(Bime, default=1, null=True, on_delete=models.CASCADE)
    Owner_Product = models.ForeignKey(Owner_Product, default=1, null=True, on_delete=models.CASCADE)
    Pictur = models.ImageField(upload_to='upload/products/')
    Img1 = models.ImageField(upload_to='upload/products/')
    Img2 = models.ImageField(upload_to='upload/products/',null=True, blank=True)
    Img3 = models.ImageField(upload_to='upload/products/',null=True, blank=True)
    Img4 = models.ImageField(upload_to='upload/products/',null=True, blank=True)
    Img5 = models.ImageField(upload_to='upload/products/',null=True, blank=True)
    Star = models.FloatField(default=0, validators=(MinValueValidator(0), MaxValueValidator(5)), null=True)
    Offer = models.BooleanField(default=False)
    OfferPrice = models.IntegerField(default=0)
    Count = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    Address = models.CharField(max_length=200, blank=False)
    Phone = models.CharField(max_length=20, blank=True)
    Date = models.DateField(default=datetime.date.today)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Product


class SliderItem(models.Model):
    Image = models.ImageField(upload_to='upload/slider/')


class News(models.Model):
    Title = models.CharField(max_length=30)
    Image = models.ImageField(upload_to='upload/news/', default='')

    def __str__(self):
        return self.Title


# Create your models here.

class Advertising1(models.Model):
    Image = models.ImageField(upload_to='upload/ads1/', default='')


class Advertising2(models.Model):
    Image = models.ImageField(upload_to='upload/ads2/', default='')


from django.db import models

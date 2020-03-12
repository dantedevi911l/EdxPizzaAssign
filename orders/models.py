from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizza_type = [('reg', 'Regular'), ('sic','Sicilian')]
    pizza_size = [('S', 'Small'), ('L', 'Large')]
    type = models.CharField(max_length=50,choices = pizza_type)
    sub_type = models.CharField(max_length=50)
    topping_quantity = models.IntegerField()
    size = models.CharField(max_length=50, choices = pizza_size)
    price = models.DecimalField(max_digits = 5,decimal_places = 2)

    def __str__(self):
        return f"{self.type}-{self.sub_type} with {self.topping_quantity} toppings at {self.size} size"

class SubAddOn(models.Model):
    addon_size = [('S', 'Small'), ('L', 'Large')]
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50, choices = addon_size)
    price = models.DecimalField(max_digits = 5,decimal_places = 2)

    def __str__(self):
        return f"{self.name} with size {self.size}"


class Subs(models.Model):
    sub_size = [('S', 'Small'), ('L', 'Large')]
    name = models.CharField(max_length=150)
    size = models.CharField(max_length=50,choices=sub_size)
    price = models.DecimalField(max_digits = 5,decimal_places = 2)

    def __str__(self):
        return f"{self.name} of {self.size} size"


class Pasta(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 5,decimal_places = 2)

    def __str__(self):
        return self.name


class Salads(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 5,decimal_places = 2)

    def __str__(self):
        return self.name


class DinnerPlatters(models.Model):
    plate_size = [('S', 'Small'), ('L', 'Large')]
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50, choices = plate_size)
    price = models.DecimalField(max_digits = 5,decimal_places = 2)

    def __str__(self):
        return f"{self.name} of size {self.size}"


class Orders(models.Model):
    pizza = models.ManyToManyField(Pizza)
    pizza_quantity = models.IntegerField()
    topping = models.ManyToManyField(Topping)
    pasta = models.ManyToManyField(Pasta)
    pasta_quantity = models.IntegerField()
    salads = models.ManyToManyField(Salads)
    salads_quantity = models.IntegerField()
    dinner_platters = models.ManyToManyField(DinnerPlatters)
    dinner_platter_quantity = models.IntegerField()
    subs = models.ManyToManyField(Subs)
    subs_quantity = models.IntegerField()
    sub_add_on = models.ManyToManyField(SubAddOn)
    total_price = models.DecimalField(max_digits = 7,decimal_places = 2)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.total_price} bought by {self.user}"

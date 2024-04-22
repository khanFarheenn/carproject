from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=150)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True, related_name='cars')

    def __str__(self):
        return f"{self.name} ({self.make} {self.model} - {self.year})"

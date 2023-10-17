from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.username

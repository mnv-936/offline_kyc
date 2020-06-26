from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    xml = models.TextField()
    dob = models.DateTimeField()
    email = models.EmailField()
    phone = models.IntegerField(default=1)

    def __str__(self):
        return self.title
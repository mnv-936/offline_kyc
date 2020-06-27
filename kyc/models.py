from django.db import models
import datetime
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=256, default = "xxx")
    dob = models.CharField(max_length=256, default = "xxx")
    address = models.CharField(max_length=256, default="xxx")
    xml = models.FileField(upload_to = 'xmls/')
    pht = models.TextField(default="xxx")
    share_code = models.IntegerField(default=1234)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class savedata_contact(models.Model):
    name =models.CharField(max_length =122)
    email =models.CharField(max_length =122)
    phone =models.CharField(max_length =122)
    message =models.CharField(max_length =122)


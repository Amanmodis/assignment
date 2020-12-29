from django.db import models
from django.core.validators import FileExtensionValidator

class default(models.Model):
    name = models.CharField(max_length=64)
    owe_name = models.CharField(max_length=64)
    owe_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    owed_by_name = models.CharField(max_length=64)
    owed_byamount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.name 

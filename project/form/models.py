from django.db import models

class form(models.Model):
    form_name=models.CharField(max_length=100)
    form_email=models.EmailField(max_length=100)
    form_number=models.CharField(max_length=100)
    form_select=models.EmailField(max_length=100)
    
# Create your models here.

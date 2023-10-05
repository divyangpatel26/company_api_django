from django.db import models


# Create your models here.
class Company(models.Model):
    comapny_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,
                            choices=(('it', 'it'), ('non-it', 'non-it'), ('Mobile Phones', 'Mobile Phones')))
    added_date = models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

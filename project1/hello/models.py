from django.db import models

# Create your models here.
class Signup(models.Model):
    firstName = models.CharField(max_length=122)
    lastName = models.CharField(max_length=122)
    Username = models.CharField(max_length=20)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=12)
    address=models.TextField()
    date= models.DateField()
    # country = models.CharField(max_length=20)
    # state = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName


from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    car_id = models.IntegerField()
    custom_need = models.CharField(max_length=250)
    car_title = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=250)
    message = models.TextField()
    user_id = models.IntegerField()
    date_add = models.DateTimeField(blank=True,auto_now_add=True)

    def __str__(self):
        return self.email
    
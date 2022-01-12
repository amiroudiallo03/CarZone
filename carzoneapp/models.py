from django.db import models
from carzone import settings
from django.db.models.signals import post_save
# Create your models here.

class Base(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Brand(Base):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name
class Transmission(Base):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Transmission'
        verbose_name_plural = 'Transmissions'

    def __str__(self):
        return self.name

class Model(Base):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    def __str__(self):
        return self.name

class Car(Base):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, related_name='car_brand', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name="car_model", on_delete=models.CASCADE)
    location =  models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.FileField(upload_to="car_image") 
    color = models.CharField(max_length=50)
    transmission = models.ForeignKey(Transmission, related_name="car_transmission", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name

# def post_save_receiver(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance, email=instance, first_name=instance, last_name=instance)

# post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
    
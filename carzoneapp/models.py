from django.db import models
from carzone import settings
from django.db.models.signals import post_save
from autoslug import AutoSlugField
from django.urls import reverse
# Create your models here.

class Base(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Banner(Base):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to="banner_image", max_length=255)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.title


class Brand(Base):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', null=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

class Transmission(Base):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', null=True)

    class Meta:
        verbose_name = 'Transmission'
        verbose_name_plural = 'Transmissions'

    def __str__(self):
        return self.name

class Model(Base):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', null=True)

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    def __str__(self):
        return self.name


class Car(Base):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', null=True)
    description = models.TextField(null=True)
    brand = models.ForeignKey(Brand, related_name='car_brand', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name="car_model", on_delete=models.CASCADE)
    location =  models.CharField(choices=state_choice,max_length=50)
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

    def get_absolute_url(self):
        return reverse("detail_view", kwargs={"slug": self.slug})
    

# def post_save_receiver(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance, email=instance, first_name=instance, last_name=instance)

# post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
class SocialNetwork(Base):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'SocialNetwork'
        verbose_name_plural = 'SocialNetworks'

    def __str__(self):
        return self.name
    
class Team(Base):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to="team_image", max_length=100, null=True, blank=True)
    job = models.CharField(max_length=50)
    social_network = models.ManyToManyField(SocialNetwork, related_name='team_network')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name

class About(Base):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to='about_image')
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.title
    
class Service(Base):
    icone = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

class Website(Base):
    logo = models.FileField(upload_to="logo_website")
    copyrights = models.CharField(max_length=50)
    title_service = models.CharField(max_length=50)
    description_service = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    web = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __str__(self):
        return self.title_service
    
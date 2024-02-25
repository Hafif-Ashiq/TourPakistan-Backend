from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField("Name_location", max_length=2000)
    history = models.TextField()
    city = models.CharField("city", max_length=1000)
    image = models.ImageField("Image", upload_to="location_images", default="none")


class Tour(models.Model):
    title = models.CharField("title", max_length=1000)
    start_city = models.CharField("start City", max_length=1000, blank=True)
    description = models.TextField()
    locations = models.ManyToManyField(Location)
    included_services = models.TextField()
    itinerary = models.TextField()
    travel_mode = models.CharField(max_length=400)
    contact_num = models.CharField(max_length=40)

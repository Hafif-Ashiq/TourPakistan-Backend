from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField("Name_location", max_length=2000)
    history = models.TextField()
    city = models.CharField("city", max_length=1000)


class LocationImage(models.Model):
    image = models.ImageField("Image", upload_to="location_images", default="none")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Tour(models.Model):
    title = models.CharField("title", max_length=1000)
    description = models.TextField()
    locations = models.ManyToManyField(Location)
    included_services = models.TextField()
    itinerary = models.TextField()
    travel_mode = models.CharField(max_length=400)
    contact_num = models.CharField(max_length=40)

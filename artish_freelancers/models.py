from django.db import models

LOCATION_CHOICES = [
    ("CA", "Canada"),
    ("US", "United States"),
    ("MX", "Mexico"),
    ("UK", "United Kingdom"),
]


# Create your models here.
class Freelancer(models.Model):
    name = models.CharField(max_length=255)
    Location = models.CharField(max_length=64, choices=LOCATION_CHOICES)
    hourly_rate_min = models.DecimalField(max_digits=10, decimal_places=0)
    hourly_rate_max = models.DecimalField(max_digits=10, decimal_places=0)
    social_links = models.ManyToManyField("SocialLink")

    about = models.TextField(max_length=4096)
    skills = models.ManyToManyField("Skill")
    tools = models.ManyToManyField("Tool")

    def __str__(self): return self.name


class Skill(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self): return self.name


class Tool(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self): return self.name


class SocialLink(models.Model):
    link = models.URLField(max_length=200)

    def __str__(self): return self.link

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)

    # address info
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    # many to many should automatically handle deletions of a favorite restaurant when that restaurant is deleted


    # contact info
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=100)

    def __str__(self):
        return self.location_name


class Store(models.Model):
    store_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50
    
    def __str__(self):
        return self.store_name

class Offer(models.Model):
    store_offer = models.ForeignKey(Store, on_delete=models.CASCADE)
    offer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.offer_text

class User(models.Model):
    user_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user_first_name = models.CharField(max_length=20)
    user_last_name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=30)
    pwd = models.CharField(max_length=100)

    def __str__(self):
        return self.user_first_name

class Order(models.Model):
    order_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date published')

class Payment(models.Model):
    pass

class PaymentType(models.Model):
    pass



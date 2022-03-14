from django.db import models

# Create your models here.




class booking1(models.Model):

    hospitsl_name = models.CharField(max_length=100)
    booking_type = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=100)
    card_no = models.IntegerField()
    bkash_no = models.IntegerField()
    address = models.CharField(max_length=100)


class hospital(models.Model):

    hospitsl_name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    Bkash_no = models.CharField(max_length=10)
    contact_no= models.IntegerField()

    







class information(models.Model):

    hospitsl_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    ICU = models.IntegerField()
    ward = models.IntegerField()
    oxygen_supply = models.CharField(max_length=10)
    contact_no= models.IntegerField






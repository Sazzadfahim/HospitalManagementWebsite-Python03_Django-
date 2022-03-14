from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class record(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    RoomNo = models.CharField(max_length=10)




class oxygensupply(models.Model):

    hospital_name = models.CharField(max_length=100)
    area = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10)



class records(models.Model):

    booking_id = models.IntegerField()
    ward = models.CharField(max_length=20)
    pyment_status = models.CharField(max_length=20)




class doctor(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    qualification = models.CharField(max_length=100)



class bookingjs(models.Model):

    hospitsl_name = models.CharField(max_length=100)
    booking_type = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)


class consult(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    dept = models.CharField(max_length=20)



class user_profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    img = models.ImageField(default="user_icon.png", null=True, blank= True )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100) 
    history = models.TextField()
    def __str__(self):
        return str(self.user)
@receiver(post_save, sender= User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile.objects.create(user=instance)
        print('profile created')
post_save.connect(create_profile, sender= User)
@receiver(post_save, sender= User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
     instance.user_profile.save()
     print('profile Updated')
post_save.connect(create_profile, sender= User)











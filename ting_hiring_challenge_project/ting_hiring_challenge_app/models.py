#<--- Ting Hiring Challenge - Imported Packages List ----

#<------Django Internal Packages-----
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
#</------Django Internal Packages-----

#</--- Ting Hiring Challenge  - Imported Packages List ----


#CustomUser Model
class CustomUser(AbstractUser):
    #Total Fields : 2
    #Total Roles : 2
    #------Custom User Table Fields------
    '''Overrides the custom django user model'''
    # Datafields
    SUPER_ADMIN = 1
    ADMIN = 2
    ROLE_CHOICES = (
      (SUPER_ADMIN,'super_admin'),
      (ADMIN,'admin'),
    )
    #This field store User's Role
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=ADMIN)
    #This field store User's Name
    name = models.CharField(max_length=264, blank='True')

#Player Master Model
class PlayerRegistration(models.Model):
    #Total Fields : 6
    #------Player Registration Table Fields------
    #This fields store player_name
    player_name = models.CharField(max_length=200,blank='True')
    #This fields store player_gender
    player_gender = models.CharField(max_length=200,blank='True')
    #This fields store player_mobile_no
    player_mobile_no = models.CharField(max_length=20,blank='True')
    #This fields store player_email
    player_email = models.CharField(max_length=100)
    #This fields store player_address
    player_address = models.TextField(max_length=900,blank=True)
    #This fields store player_retry
    player_retry = models.BooleanField(default=True)
    #This fields store created_at
    created_at = models.DateTimeField(default=timezone.now,blank='True')
    #This fields store updated_at
    updated_at = models.DateTimeField(default=timezone.now,blank='True')

    def __str__(self):
        return str(self.pk)

#Player Winning Model - This table stores the Winning History of Each Player
class PlayerWinnings(models.Model):
    #Total Fields : 4
    #------Player Winning Table Fields------
    #This fields is a Foreign Key with Player Registration Model.
    player_name = models.ForeignKey(PlayerRegistration, on_delete = models.CASCADE)
    #This fields store player_winning
    player_winning = models.CharField(max_length=100)
    #This fields store created_at
    created_at = models.DateTimeField(default=timezone.now,blank='True')
    #This fields store updated_at
    updated_at = models.DateTimeField(default=timezone.now,blank='True')

    def __str__(self):
        return str(self.pk)

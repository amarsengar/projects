from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=None,primary_key=True)
    about = models.CharField(max_length=150,default=' ')
    city = models.CharField(max_length=64,default='')
    contact = models.IntegerField(default=0)
    head_snap = models.ImageField(upload_to='profile_images',blank=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.get_or_create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

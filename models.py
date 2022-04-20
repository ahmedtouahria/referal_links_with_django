from django.contrib.auth.models import User
from django.db import models
from .utils import generate_random_code

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_path_profile, default=None, null=True, blank=True)
    code = models.CharField(max_length=12,blank=True)
    recommended_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='ref_by')
    isPartner = models.BooleanField(default=False)
    profit=models.FloatField(default=0.0)
    def __str__(self):
        return str(self.user)
    def country(self):
        return self.user.country
    def num_of_partner(self):
        partners = Profile.objects.filter(isPartner=True)
        return len(partners)       
        
        
    def save(self, *args, **kwargs):
       if self.code=='':
           code = generate_random_code()
           self.code=code
       super().save(*args, **kwargs) # Call the real save() method

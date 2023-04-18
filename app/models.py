from django.db import models

# Create your models here.
class OPSEmp(models.Model):
    badge_id=models.CharField(max_length=25,blank=False,null=False)
    department=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25,blank=False,null=False)
    
    def __str__(self) :
        return self.badge_id
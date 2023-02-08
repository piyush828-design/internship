from django.db import models
# Create your models here.
#from django.db import models
#from django.contrib.auth.models import User

#class Post(models.Model):
  # user = models.ForeignKey(User,on_delete=models.CASCADE)
   #post_title = models.CharField(max_Length=70)
   #post_cat = models.CharField(max_Length=70)
  # post_publish_date = models.DateField()


created_at= models.DateField(auto_now_add=True)
updated_at =models.DateField(auto_now  = True)
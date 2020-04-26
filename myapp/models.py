from django.db import models

# Create your models here.
class Trial(models.Model):
	name= models.CharField(max_length=100)
	body= models.TextField()
	email= models.EmailField(max_length=100)

	city=models.CharField(max_length=100)
	profile_image = models.ImageField(upload_to='images/')

class SignUp(models.Model):
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	
	city=models.CharField(max_length=100)
	
	def __str__(self):
		return self.name 
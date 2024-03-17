from django.db import models

# Create your models here.

class Countries(models.Model):
	cities = models.CharField(max_length=200)
	
	def __str__(self):
		return self.cities


class Weather_info(models.Model):
	city = models.ForeignKey(Countries, on_delete = models.CASCADE)
	temperature = models.DecimalField(max_digits = 50, decimal_places = 2)
	conditions = models.CharField(max_length = 50)

	def __str__(self):
		return self.conditions
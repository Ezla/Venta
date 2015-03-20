from django.db import models


class Productos(models.Model):
	codigo = models.CharField(max_length=20)
	nombre = models.CharField(max_length=50)
	precio_unit = models.FloatField()

	def __unicode__(self):
		return self.nombre
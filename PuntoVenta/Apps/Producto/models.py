from django.db import models
from django.core.exceptions import ValidationError

class Producto(models.Model):
	codigo = models.CharField(max_length=48, unique=True)
	descripcion = models.CharField(max_length=100)
	punitario = models.DecimalField(max_digits=8, decimal_places=2)
	pmayoreo = models.DecimalField(max_digits=8, decimal_places=2)
	inventario = models.BooleanField(default=False)
	cantidad = models.IntegerField(null=True, blank=True)
	minimo = models.IntegerField(null=True, blank=True)


	def __unicode__(self):
		return self.descripcion

	def clean(self):
		errores = {}
		cont = 0

		if len(self.codigo) < 3:
			errores.update({'codigo':'El codigo de barras debe contener mas de tres caracteres.'})
			cont = 1
		#---punitario---
		if self.punitario < self.pmayoreo:
			errores.update({'punitario':'El precio unitario debe ser mayor que el precio  por mayoreo.'})
			cont = 1
		if self.punitario < 0:
			errores.update({'punitario':'Este campo no puede contener numeros negativos.'})
			cont = 1
		#---pmayoreo---
		if self.punitario < self.pmayoreo:
			errores.update({'pmayoreo':'El precio por mayoreo debe ser menor al precio unitario.'})
			cont = 1
		if self.pmayoreo < 0:
			errores.update({'pmayoreo':'Este campo no puede contener numeros negativos.'})
			cont = 1
		#---inventario---
		if self.inventario == True:
			#---cantidad---
			if self.cantidad == None:
				errores.update({'cantidad':'Si activas la opcion de inventario. Este campo es obligatorio.'})
				cont = 1
			elif self.cantidad < 0:
				errores.update({'cantidad':'Este campo no puede contener numeros negativos.'})
				cont = 1
			#---minimo---
			if self.minimo == None:
				errores.update({'minimo':'Si activas la opcion de inventario. Este campo es obligatorio.'})
				cont = 1
			elif self.minimo < 0:
				errores.update({'minimo':'Este campo no puede contener numeros negativos.'})
				cont = 1

		if cont == 1:
			raise ValidationError(errores)
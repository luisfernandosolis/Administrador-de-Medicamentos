from django.db import models

# Create your models here.

#tipo de medicamento
class typeOfMedication(models.Model):
	name=models.CharField(max_length=1)
	def __str__(self):
		return '{}'.format(self.name)
#tipo de presentacion
class typeOfPresentation(models.Model):
	name=models.CharField(max_length=3)
	def __str__(self):
		return '{}'.format(self.name)

#registro de medicamentos
class Medication(models.Model):
	#informacion particular
	code=models.CharField(max_length=100,blank=True,null=True)
	#code=models.IntegerField()
	typeMedication = models.ManyToManyField(typeOfMedication,null=True,blank=True)
	name=models.CharField(max_length=100)
	typePresentation = models.ManyToManyField(typeOfPresentation,null=True,blank=True)
	price=models.FloatField()

	#informe de consumo
	balance=models.IntegerField(default=0,null=True,blank=True)
	ingreso=models.IntegerField(default=0,null=True,blank=True)
	ventaexterna=models.IntegerField(default=0,blank=True,null=True)
	valorE=models.FloatField(default=0.0,blank=True,null=True)
	ventasis=models.IntegerField(default=0,blank=True,null=True)
	valorS=models.FloatField(default=0.0,blank=True,null=True)
	int_sanitaria=models.IntegerField(default=0,blank=True,null=True)
	exo=models.IntegerField(default=0,blank=True,null=True)
	transferencia=models.IntegerField(default=0,blank=True,null=True)
	totalsalida=models.IntegerField(default=0,blank=True,null=True)
	saldoDisponible=models.IntegerField(default=0,blank=True,null=True)
	fecha_expedicion=models.CharField(max_length=30,blank=True,null=True)


	def __str__(self):
		return '{}'.format(self.name)

#tipo de venta (sis o externo)
class TipoVenta(models.Model):
	tipo=models.CharField(max_length=10) 
	def __str__(self):
		return self.tipo

#registro de ventas
class VentasMes(models.Model):
	nombre=models.CharField(max_length=80 ,blank=True, null=True)
	cantidad=models.IntegerField(default=0)
	tipo=models.ManyToManyField(TipoVenta,null=True,blank=True)
	def __str__(self):
		return self.nombre


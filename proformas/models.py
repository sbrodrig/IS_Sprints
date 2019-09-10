from django.db import models
from personas_juridicas.models import Juridica

# Create your models here.
class Proforma(models.Model):
	codigo=models.CharField(max_length=20)
	version=models.PositiveIntegerField()
	nombreProforma=models.CharField(max_length=100)
	tipoEmpresa=models.CharField(max_length=20)
	empresa=models.ForeignKey(Juridica, on_delete=models.CASCADE)
	sector=models.CharField(max_length=20)
	fechaSolicitud=models.CharField(max_length=30)
	fechaEnvio=models.CharField(max_length=30)
	numeroParticipantes=models.PositiveIntegerField()
	horas=models.PositiveIntegerField()
	cantidadCursos=models.PositiveIntegerField()
	estado=models.CharField(max_length=30)
	porcentExito=models.FloatField()
	porcentDesc=models.FloatField()
	montoProforma=models.FloatField()
	montoDesc=models.FloatField()
	observacion=models.CharField(max_length=500)
	anexos=models.FileField(upload_to='uploads/',null=True,blank=True)
	nombre=models.CharField(max_length=50)
	fechaRespuesta=models.CharField(max_length=30,blank=True, null=True)
	montoAceptado=models.FloatField(blank=True,null=True)
	montoEjecutado=models.FloatField(blank=True,null=True)
	montoPorEjecutarse=models.FloatField(blank=True,null=True)
	
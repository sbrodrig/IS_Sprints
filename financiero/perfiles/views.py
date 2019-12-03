from django.shortcuts import render, redirect
from financiero.presupuestos.models import PresupuestoEvento
from financiero.orden_facturacion.models import OrdenFacturacion
from django.http import JsonResponse, HttpResponseRedirect


# Create your views here.

def index(request):
	return render(request, 'perfiles_index.html')

def index_analista(request):
	return render(request, 'base_analista.html')

def index_coordinador(request):
	return render(request, 'base_coordinador.html')

def por_aprobar(request):
	presupuestos_ev = PresupuestoEvento.objects.filter(estado=None)
	orden_fact=OrdenFacturacion.objects.filter(estado='SLCE')
	return render(request, 'por_aprobar.html', {"presupuestos_ev":presupuestos_ev, "orden_fact":orden_fact})

def aprobar_orden_fact(request, pk):
	orden=OrdenFacturacion.objects.get(pk=pk)
	orden.estado="ACPF"
	orden.save()
	return HttpResponseRedirect("/financiero/perfiles/pendiente_aprobacion/")

def anular_orden_fact(request, pk):
	orden=OrdenFacturacion.objects.get(pk=pk)
	orden.estado="ANLD"
	orden.save()
	return HttpResponseRedirect("/financiero/perfiles/pendiente_aprobacion/")
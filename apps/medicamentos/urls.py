from django.urls import path
from . import views



app_name='medicamentos'

urlpatterns = [
	
	path('',views.home,name="home"),
	path('home/',views.ListMedication,name='list_medications'),
	path('vender/',views.search,name="vender"),
	path('añadir/',views.añadir,name='añadir'),
	path('nuevo/',views.AñadirMedicamento,name='nuevo'),
	path('operar/<int:pk>',views.vender, name='operar'),
	path('ingreso/<int:pk>',views.ingreso, name='ingreso'),
	path('reporte/',views.reporte,name='reporte'),
	path('reportepdf/',views.reporte_Medications,name='reporte_Medications')

]

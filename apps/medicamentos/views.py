from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView,ListView
from django.http import HttpResponse
from django.urls import reverse_lazy # 
from django.contrib.auth.decorators import login_required


from .models import Medication,typeOfMedication,typeOfPresentation,VentasMes
from .forms import formsearch,formOperacionVender,VentaForm,IngresarForm,NewMedication
from .filters import UserFilter
from .reportes import ReporteMedicamentos



#para generar el reporte
from io import BytesIO
from reportlab.lib.pagesizes import A4,landscape
from reportlab.pdfgen  import canvas
from reportlab.platypus import (
        Paragraph, 
        Table, 
        SimpleDocTemplate, 
        Spacer, 
        TableStyle, 
        Paragraph)

from reportlab.lib.styles import ParagraphStyle, TA_CENTER,TA_LEFT
from reportlab.lib.units import inch, mm
from reportlab.lib import colors



# Create your views here.
def home(request):
	return redirect('user:logout')

#para listar los medicamentos
@login_required # se necesita estar logueado para acceder a esta vista
def ListMedication(request):
	list_medicatios=Medication.objects.all()
	context={
		'medications':list_medicatios
	}
	return render(request,'medications.html',context)

#para buscar elemento en el modelo en 'vender'
@login_required # se necesita estar logueado para acceder a esta vista
def search(request):


	user_list = Medication.objects.all()
	user_filter = UserFilter(request.GET, queryset=user_list)
	
	return render(request, 'busquedaVender.html', {'filter': user_filter})

@login_required # se necesita estar logueado para acceder a esta vista
def añadir(request):
	user_list = Medication.objects.all()
	user_filter = UserFilter(request.GET, queryset=user_list)
	return render(request, 'busquedaañadir.html', {'filter': user_filter})
@login_required # se necesita estar logueado para acceder a esta vista
def reporte(request):
	user_list = Medication.objects.all().order_by('name')
	user_filter = UserFilter(request.GET, queryset=user_list)

	return render(request, 'reporte.html', {'filter': user_filter})
@login_required # se necesita estar logueado para acceder a esta vista
def vender(request,pk):
	bandera=False
	medicamentos=Medication.objects.get(id=pk)
	if request.method=="POST":
		form=VentaForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			datos=form.cleaned_data
			tipo=datos.get('tipo')[0]
			
			cantidad=datos.get('cantidad')
			if(str(tipo) == 'SIS'):
				medicamentos.ventasis+=cantidad
				#---si queremos que cueste algo con SIS
				#valor_venta=cantidad*medicamentos.price #valor por vender 'n'  medicamentos
				#medicamentos.valorS=medicamentos.valorS+valor_venta
				print(medicamentos.valorS)
				medicamentos.save()
				
			elif(str(tipo)=="v. externa"):
				medicamentos.ventaexterna+=cantidad
				valor_venta=cantidad*medicamentos.price #valor por vender 'n'  medicamentos
				medicamentos.valorE=medicamentos.valorE+valor_venta
				print(medicamentos.valorE)
				medicamentos.save()
			elif(str(tipo)=="int. sanit"):
				medicamentos.int_sanitaria=medicamentos.int_sanitaria+cantidad
			elif(str(tipo)=="exo"):
				medicamentos.exo=medicamentos.exo+cantidad
			elif(str(tipo)=="Transf"):
				medicamentos.transferencia=medicamentos.transferencia+cantidad
			saldo=(medicamentos.ingreso+medicamentos.balance)-cantidad
			if(cantidad>=0 and saldo>0):
				total_de_salida=medicamentos.ventaexterna+medicamentos.ventasis+medicamentos.transferencia+medicamentos.exo+medicamentos.int_sanitaria
				#medicamentos.ingreso=medicamentos.ingreso-int(datos.get('cantidad'))
				medicamentos.totalsalida=total_de_salida
				medicamentos.saldoDisponible=(medicamentos.balance+medicamentos.ingreso)-(total_de_salida)
				medicamentos.save()
				return redirect('medicamentos:list_medications')
			else:
				form=VentaForm()
				bandera=True

				
	else:
		form=VentaForm()
	context={
		'form':form,
		'mensaje':'Cantidad ingresada incorrecta o no hay suficiente medicamento para vender dicha cantidad',
		'bandera':bandera
	}
	return render(request,'formvender.html',context)
@login_required # se necesita estar logueado para acceder a esta vista
def ingreso(request,pk):
	medicamentos=Medication.objects.get(id=pk)
	if request.method=="POST":
		form=IngresarForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			datos=form.cleaned_data
			medicamentos.ingreso=datos.get('ingreso')
			medicamentos.fecha_expedicion=datos.get('fecha_expedicion')
			medicamentos.saldoDisponible=(medicamentos.ingreso+medicamentos.balance)-(medicamentos.ventaexterna+medicamentos.ventasis+medicamentos.exo+medicamentos.int_sanitaria+medicamentos.transferencia)
			medicamentos.save()
			return redirect('medicamentos:añadir')
	else:
		form=IngresarForm(instance=medicamentos)
	context={
		'form':form
	}
	return render(request,'formingresar.html',context)
@login_required # se necesita estar logueado para acceder a esta vista
def AñadirMedicamento(request):
	if request.method=="POST":
		form=NewMedication(request.POST)
		if form.is_valid():
			form.save()
			return redirect('medicamentos:list_medications')
	else:
		form=NewMedication()
	context={
		'form':form
	}
	return render(request,'añadirmedicamento.html',context)




#generar reporte pdf
@login_required # se necesita estar logueado para acceder a esta vista


def reporte_Medications(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="medicamentos.pdf"'
	r = ReporteMedicamentos()
	response.write(r.run())
	return response

    
'''
    buf=BytesIO()
    #cmontamos un canbas en el buffer de datos
    c=canvas.Canvas(buf,pagesize=landscape(A4))
    saldo_final='201902'
    #HEADER
    c.setLineWidth(0.1)
    c.setFont('Helvetica',9)
    c.drawString(15,570,'Red:')
    c.drawString(90,570,'HUAMANGA:')
    c.drawString(15,560,'MicroRed:')
    c.drawString(90,560,'OCROS:')
    c.drawString(15,550,'Establecimiento:')
    c.drawString(90,550,'PS. CHUMBES:')
    c.drawString(180,550,'Saldos Finales: {}'.format(saldo_final))

    data = [["Código","Tipo","Nombre","Presentación","Precio",'saldo','ingreso','V.Ext','Valor',"SIS",'valor','int.Sanit','EXO','Transf.','Total sal.','Saldo disp.','Fec. Exp.']] \
            +[[x.code,x.typeMedication.all()[0],x.name, x.typePresentation.all()[0], x.price,x.balance,x.ingreso,x.ventaexterna,x.valorE,x.ventasis,x.valorS,x.int_sanitaria,x.exo,x.transferencia,x.totalsalida,x.saldoDisponible,x.fecha_expedicion] 
                for x in Medication.objects.all().order_by('name')]

    style = TableStyle([
        ('GRID', (0,0), (-1,-1), 0.25, colors.black),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE')])

    #escribimos la tabla
    width,height=landscape(A4)
    table=Table(data)
    table.setStyle(style)
    table.wrapOn(c,width,height)
    table.drawOn(c,2,800-len(data))
    c.showPage()
    c.save()








    pdf=buf.getvalue()
    buf.close()
    response.write(pdf)
'''
 #direccion del logo que esta en /media/sismed.jpg
 
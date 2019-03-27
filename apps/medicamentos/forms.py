from django import forms
from .models import Medication,VentasMes,typeOfMedication
class formsearch(forms.Form):
	name=forms.CharField()




class DateInput(forms.DateInput):
    input_type = 'date'

class IngresarForm(forms.ModelForm):
	class Meta:
		model = Medication
		fields = ['code','name','typePresentation','price','ingreso','fecha_expedicion']
		labels={
			'code':'Codigo',
			'name':'Nombre',
			'typePresentation':'Presentación',
			'price':'Precio actual',
			'ingreso':'Ingrese la cantidad de medicamentos a recargar.',
			'fecha_expedicion':'Fecha de Expedición'
		}
		widgets = {
			'code':forms.TextInput(attrs={'class':'form-control'}),
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'typePresentation':forms.SelectMultiple(attrs={'class':'form-control'}),
			'price':forms.TextInput(attrs={'class':'form-control'}),
			'ingreso':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_expedicion':forms.DateInput(attrs={'type': 'date'})
		}
	def __init__(self, *args, **kwargs):
	        super(IngresarForm, self).__init__(*args, **kwargs)
	        for field in iter(self.fields):
	            self.fields[field].widget.attrs.update({
	                'class': 'form-control'
	            })




class NewMedication(forms.ModelForm):
	class Meta:
		model=Medication
		exclude=['ingreso','ventaexterna','valorE','ventasis','valorS','totalsalida','saldoDisponible']
		fields=[
			'code',
			'typeMedication',
			'name',
			'typePresentation',
			'price',
			'balance'
		]
		labels={
			'code':'Codigo',
			'typeMedication':'Tipo de Medicamento',
			'name':'Nombre',
			'typePresentation':'Presentación',
			'price':'Precio',
			'balance':'Cantidad inicial en farmacia (saldo)'

		}

	def __init__(self, *args, **kwargs):
	        super(NewMedication, self).__init__(*args, **kwargs)
	        for field in iter(self.fields):
	            self.fields[field].widget.attrs.update({
	                'class': 'form-control'
	            })

class formOperacionVender(forms.ModelForm):

	class Meta:
		model=Medication
		exclude=['typeMedication','typePresentation']
		# los campos del modelo que se van a mostrar
		fields=[
			'code',
			'name',
			'price',
			'balance',
			
		]
		# como queremos que sean los Labels de cada campo
		labels={
			'code':'Codigo',
			'name':'Nombre',
			'price':'Precio',
			'balance':'Saldo',
			
		}

		#definimos el campo 'HTML' de cada label
		#attrs: los atributos de cada campo
		widgets={
			'code':forms.TextInput(attrs={'class':'form-control'}),
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'price':forms.TextInput(attrs={'class':'form-control'}),
			'balance':forms.TextInput(attrs={'class':'form-control'}),
		}

class VentaForm(forms.ModelForm):

    class Meta:
        model = VentasMes
        fields = ['cantidad','tipo']

    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })



		

   

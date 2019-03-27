from django.contrib import admin
from .models import Medication,typeOfMedication,typeOfPresentation,VentasMes,TipoVenta
# Register your models here.
class MedicationRegister(admin.ModelAdmin):
	class Meta:
		model=Medication

admin.site.register(Medication,MedicationRegister)

class typeOfMedicationRegister(admin.ModelAdmin):
	class Meta:
		model=typeOfMedication
admin.site.register(typeOfMedication,typeOfMedicationRegister)
class typeOfPresentationRegister(admin.ModelAdmin):
	class Meta:
		model=typeOfPresentation
admin.site.register(typeOfPresentation,typeOfMedicationRegister)
class VentasMesRegister(admin.ModelAdmin):
	class Meta:
		model=VentasMes
admin.site.register(VentasMes,typeOfMedicationRegister)
class TipoVentaRegister(admin.ModelAdmin):
	class Meta:
		model=TipoVenta
admin.site.register(TipoVenta,TipoVentaRegister)

'''
class InformedeConsumoRegister(admin.ModelAdmin):
	class Meta:
		model=InformedeConsumo
admin.site.register(InformedeConsumo,InformedeConsumoRegister)
'''
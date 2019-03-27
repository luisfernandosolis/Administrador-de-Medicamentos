from io import BytesIO
import os
from reportlab.lib.pagesizes import A4,landscape
from reportlab.pdfgen  import canvas
from reportlab.lib.styles import ParagraphStyle, TA_CENTER,TA_LEFT
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import (
        Paragraph, 
        Table, 
        SimpleDocTemplate, 
        Spacer, 
        TableStyle, 
        Paragraph)

from .models import Medication
from reportlab.lib.utils import ImageReader
from PIL import Image
from reportlab.platypus import Image

from django.conf import settings
class ReporteMedicamentos(object):

    def __init__(self):
        self.buf = BytesIO()
        #direccion del logo que esta en /media/sismed.jpg
        self.logo_filename = settings.MEDIA_ROOT + os.sep + "sismed.png"

    def run(self):
        

        self.doc = SimpleDocTemplate(self.buf)
        self.story = []
        #self.encabezado()
        self.crearTabla()
        self.doc.pagesize = landscape(A4)
        self.doc.build(self.story, onFirstPage=self.numeroPagina, 
            onLaterPages=self.numeroPagina)
        pdf = self.buf.getvalue()
        self.buf.close()
        return pdf

    def encabezado(self):
        style = self.estiloPC()
    
        bogustext = ("Red: HUAMANGA")
        p = Paragraph(bogustext, style)
        self.story.append(p)
        self.story.append(Spacer(1,0.01*inch))
        bogustext = ("MicroRed: Ocros")
        p = Paragraph(bogustext, style)
        self.story.append(p)

        bogustext = ("Establecimiento: 03579: P.S CHUMBES")
        p = Paragraph(bogustext, style)
        self.story.append(p)


        

    def crearTabla(self):
        data = [["Código","Tipo","Nombre","Presentación","Precio",'saldo','ingreso','V.Ext','Valor',"SIS",'valor','int.Sanit','EXO','Transf.','Total sal.','Saldo disp.','Fec. Exp.']] \
            +[[x.code,x.typeMedication.all()[0],x.name, x.typePresentation.all()[0], x.price,x.balance,x.ingreso,x.ventaexterna,x.valorE,x.ventasis,x.valorS,x.int_sanitaria,x.exo,x.transferencia,x.totalsalida,x.saldoDisponible,x.fecha_expedicion] 
                for x in Medication.objects.all().order_by('name')]

        style = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE')])

        t = Table(data,repeatRows=1)
        #agregamos repeat rows para que el encabezado se repita la primera fila de 'data' en cada salto de pagina
        t.setStyle(style)
        self.story.append(t)

    def estiloPC(self):
        return ParagraphStyle(name="centrado",fontSize=10,leftIndent=0,alignment=TA_LEFT)

    def numeroPagina(self,canvas,doc):
        num = canvas.getPageNumber()
        text = "Página %s" % num
        saldo_final='201902' #dinamica
        fecha_footer='martes, 5 de marzo del 2019' #dinamica
        #HEADER
        canvas.setLineWidth(0.1)
        canvas.setFont('Helvetica',9)
        canvas.drawString(15,570,'Red:')
        canvas.drawString(90,570,'HUAMANGA:')
        canvas.drawString(15,560,'MicroRed:')
        canvas.drawString(90,560,'OCROS:')
        canvas.drawString(15,550,'Establecimiento:')
        canvas.drawString(90,550,'PS. CHUMBES:')
        canvas.drawString(180,550,'Saldos Finales: {}'.format(saldo_final))
        canvas.line(10, 70, 830, 70)
        canvas.rect(440,45,50,15)
        canvas.drawString(370,50,'Sub Total Venta')
        canvas.drawString(10,50,fecha_footer)
        #logo
        canvas.drawInlineImage(self.logo_filename, 700,540 ,100,30)
        canvas.drawString(690,530,'Informe de consumo Integrado ICI')
        canvas.drawRightString(800, 50, text)
 

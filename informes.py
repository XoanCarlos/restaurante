from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
import servicios
import bbdd
import locale

""" Modulo generardor de documentos

"""





def cabecera(cser):
    """ Crea la cabecera del documento

        Esta cabecera mostrara los datos principales de la empresa
        que se repetirá en todos los documentos

    """
    try:
        cser.setTitle('Informes')
        cser.setAuthor('El profesor')
        cser.setFont('Helvetica', size=11)
        cser.line(50, 820, 525, 820)
        cser.line(50, 745, 525, 745)
        textnom = 'RESTAURANTE TEIS'
        textdir = 'Avenida Galicia, 101 - Vigo'
        texttlfo = '886 12 04 64'
        cser.drawString(255, 795, textnom)
        cser.drawString(245, 775, textdir)
        cser.drawString(280, 755, texttlfo)
    except:
        print ('erros cabecera')

def pie(cser):
    """ Crea el pie del documento

        El pie mostrará el agradecimiento al cliente
        y la fecha de creación del documento y nº de pagina si fuese necesario

    """
    try:
        cser.line(50, 20, 525, 20)
        textgracias = "Gracias por su visita"
        cser.drawString(270, 10, textgracias)

    except:
        print('erros pie')

def reportservicios():
    """ Listado de servicios ofrecidos

        Este módulo genera un listado del codigo, nombre del servidio y precios que
        ofrece el restaurante

    """

    try:
        cser = canvas.Canvas('servicios.pdf', pagesize=A4)
        cabecera(cser)
        pie(cser)
        textlistado = 'LISTADO DE SERVICIOS'
        cser.drawString(255, 705, textlistado)
        cser.line(50,700,525,700)
        x = 50
        y = 680
        listado = servicios.mostrarservicios()
        for registro in listado:
            for i in range(3):
                cser.drawString(x,y,str(registro[i]))
                x = x + 220
            y = y -20
            x = 50
        cser.showPage()
        cser.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/servicios.pdf')

    except:
        print('error en informe')


def factura(idfactura):

    """ Crea la factura para el cliente

        Este documento crea la factura. Necesita acceder a dos tablas (join), la propia de la factura y
        la tabla de servicio para obtener los nombres de las comandas y precios y asi generar
        los totales y subtotales. Hay ajustes para una mejor alineacion de la presentacion

    """

    try:
        cser = canvas.Canvas( str(idfactura) + '.pdf', pagesize=A4)

        cabecera(cser)
        pie(cser)
        bbdd.cur.execute('select idventa, s.servicio, cantidad, s.precio from comandas c, servicios s where c.idfactura = ? and s.Id = c.idservicio', (idfactura,))
        listado = bbdd.cur.fetchall()
        bbdd.conexion.commit()
        textlistado = 'Factura'
        cser.drawString(255, 705, textlistado)
        cser.line(50, 700, 525, 700)
        x = 50
        y = 680
        total = 0
        for registro in listado:
            for i in range(4):
                if i <= 1:
                    cser.drawString(x, y, str(registro[i]))
                    x = x + 40
                else:
                    x = x + 120
                    cser.drawString(x, y, str(registro[i]))


                var1 = int(registro[2])
                var2 = registro[3].split()[0]
                var2 = locale.atof(var2)
                var2 = round(float(var2), 2)
                subtotal = var1*var2
            total = total + subtotal
            subtotal = locale.currency(subtotal)
            x = x + 120
            cser.drawString(x, y, str(subtotal))
            y = y - 20
            x = 50
        y = y -20
        cser.line(50, y, 525, y)
        y = y -20
        x = 400
        cser.drawString(x, y, 'Total: ')
        x = 485
        total = round(float(total), 2)
        total = locale.currency(total)
        cser.drawString(x,y,str(total))
        cser.showPage()
        cser.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/' + str(idfactura) + '.pdf')


    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()
        print('error en factura')


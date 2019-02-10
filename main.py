import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk
import bbdd
import servicios
import informes
import clientes
import camareros
import mesas
import time
import reservas

class Restaurante():

    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('ventana.glade')
        self.vprincipal = b.get_object('principal')

        """ botones sala """
        self.btnmesa1 = b.get_object('btnmesa1')
        self.btnmesa2 = b.get_object('btnmesa2')
        self.btnmesa3 = b.get_object('btnmesa3')
        self.btnmesa4 = b.get_object('btnmesa4')
        self.btnmesa5 = b.get_object('btnmesa5')
        self.btnmesa6 = b.get_object('btnmesa6')
        self.btnmesa7 = b.get_object('btnmesa7')
        self.btnmesa8 = b.get_object('btnmesa8')

        """ widgets entry """
        self.entservicio = b.get_object('entservicio')
        self.entprecio = b.get_object('entprecio')
        self.entdni = b.get_object('entdni')
        self.entapel = b.get_object('entapel')
        self.entnome = b.get_object('entnome')
        self.entdir = b.get_object('entdir')
        self.entcam = b.get_object('entcam')
        self.entpass = b.get_object('entpass')
        self.entpassr = b.get_object('entpassr')
        self.entmesa = b.get_object('entmesa')
        self.entidmesa = b.get_object('entidmesa')
        self.entclifac = b.get_object('entclifac')
        self.entcamfac = b.get_object('entcamfac')
        self.entmesafac = b.get_object('entmesafac')
        self.entfechafac = b.get_object('entfechafac')
        self.entserfac = b.get_object('entserfac')
        self.entcantidad = b.get_object('entcantidad')
        self.entpago = b.get_object('entpago')
        
        """ widgets liststores and treeviews 
        
        """
        self.listservicios = b.get_object('listservicios')
        self.treeservicios = b.get_object('treeservicios')
        self.listclientes = b.get_object('listclientes')
        self.treeclientes = b.get_object('treeclientes')
        self.treecamareros = b.get_object('treecamareros')
        self.treemesas = b.get_object('treemesas')
        self.treefacturas = b.get_object('treefacturas')
        self.treecomandas = b.get_object('treecomandas')
        self.cmbprov = b.get_object('cmbprov')
        self.cmbmuni = b.get_object('cmbmuni')
        self.listprov = b.get_object('listprov')
        self.listmuni = b.get_object('listmuni')
        self.listcamareros = b.get_object('listcamareros')
        self.listmesas = b.get_object('listmesas')
        self.listfact = b.get_object('listfact')
        self.listcomandas = b.get_object('listcomandas')


        dic = {'on_principal_destroy': self.salir, 'on_btnaltaser_clicked': self.altaser,
               'on_btnsalir_clicked': self.salir, 'on_btnrepser_clicked': self.reporserv,
               'on_treeservicios_cursor_changed': self.cargaservicio, 'on_btnbajaser_clicked': self.bajarserv,
               'on_btnmodifser_clicked': self.modifserv, "on_cmbprov_changed": self.cargamuni,
               "on_btnaltacli_clicked": self.altacli, "on_treeclientes_cursor_changed": self.cargarcliente,
               'on_btnbajcli_clicked': self.bajacliente, 'on_btnmodifcli_clicked': self.modifcliente,
               "on_btnactualizar_clicked": self.renovar, 'on_btnaltacam_clicked': self.altacam,
               'on_treecamareros_cursor_changed': self.cargarcamarero, 'on_btnbajacam_clicked': self.bajacam,
               "on_btnmodifcam_clicked": self.modifcam, 'on_btnaltmesa_clicked': self.altamesa,
               'on_treemesas_cursor_changed': self.cargarmesas, 'on_btnmodifmesa_clicked': self.modifmesa,
               'on_btnbajamesa_clicked': self.bajamesa, 'on_treefacturas_cursor_changed': self.cargarreserva,
               "on_btnmesa1_clicked": self.mesa1, 'on_btnmesa2_clicked': self.mesa2,
               'on_btnaltacomanda_clicked': self.altacomanda, 'on_btnfactura_clicked': self.factura,
               }


        """ label usados """
        self.lblcodigo = b.get_object('lblcodigo')
        self.lblcodcam = b.get_object('lblcodcam')
        self.lblcodmesa = b.get_object('lblcodmesa')
        self.lblfac = b.get_object('lblfac')

        """ widgets varios"""
        self.notebook = b.get_object('notebook')

        """ lista de widgets """
        self.listaservicios = [ self.lblcodigo, self.entservicio, self.entprecio ]
        self.listaclientes = [ self.entdni, self.entapel, self.entnome, self.entdir]
        self.liscmb = [ self.cmbprov, self.cmbmuni ]
        self.listacam = [ self.entcam, self.entpass, self.entpassr ]
        self.listamesa = [ self.entidmesa, self.entmesa ]
        self.listareserva = [ self.lblfac, self.entclifac, self.entcamfac, self.entmesafac, self.entfechafac, self.entpago ]

        self.reservas = { 'mesa1': 0, 'mesa2': 0, 'mesa3': 0, 'mesa4' : 0, 'mesa5' : 0, 'mesa6' : 0, 'mesa6' : 0, 'mesa6' : 0, 'mesa7' : 0, 'mesa8': 0 }
        self.mesas = [ self.btnmesa1, self.btnmesa2, self.btnmesa3, self.btnmesa4, self.btnmesa5, self.btnmesa6, self.btnmesa7, self.btnmesa8 ]

        """ mostramos la ventana """

        b.connect_signals(dic)
        color = Gdk.color_parse('#ADD8E6')
        rgba = Gdk.RGBA.from_color(color)
        self.vprincipal.override_background_color(0, rgba)

        self.vprincipal.show()
        self.vprincipal.maximize()
        #self.vprincipal.fullscreen()
        self.listarservicios()
        self.listarclientes()
        self.cargarprov()
        self.listarcamareros()
        self.listarmesas()
        self.iniciarsala()
        self.hoy = time.strftime("%d/%m/%Y")


        """ funciones servicios """
    def altaser(self, widget):
        self.servicio = self.entservicio.get_text()
        self.precio = self.entprecio.get_text()
        servicios.altaser(self.servicio, self.precio)
        self.listarservicios()
        self.limpiarserv()

    def bajarserv(self, widget):
        self.codigo = self.lblcodigo.get_text()
        servicios.bajaservicio(self.codigo)
        self.listarservicios()
        self.limpiarserv()

    def modifserv(self, widget):
        self.filaser = []
        for i in range(3):
            self.filaser.append(self.listaservicios[i].get_text())

        servicios.modifservicios(self.filaser)
        self.listarservicios()
        self.limpiarserv()

    def listarservicios(self):
        listado = servicios.mostrarservicios()
        self.listservicios.clear()
        for registro in listado:
            self.listservicios.append(registro)

    def reporserv(self, widget):
        informes.reportservicios()

    def cargaservicio(self, widget):
        servicios.cargarservicio(self.listaservicios, self.treeservicios, self.entserfac)


    def limpiarserv(self):
        for registro in self.listaservicios:
            registro.set_text('')

    """ funciones clientes """

    def cargarprov(self):
        clientes.cargarprovi(self.listprov)

    def cargamuni(self, widget):
        clientes.cargamuni(self.listmuni, self.cmbprov)

    def altacli(self, widget):
        #falta comprobación dni
        self.registrocli = []
        self.liscmb = []
        indexp = self.cmbprov.get_active()
        modelp = self.cmbprov.get_model()
        itemp = modelp[indexp][0]
        indexm = self.cmbmuni.get_active()
        modelm = self.cmbmuni.get_model()
        itemm = modelm[indexm][0]
        self.liscmb =[ itemp, itemm ]
        for i in range(4):
            self.registrocli.append(self.listaclientes[i].get_text())
        self.registrocli = self.registrocli + self.liscmb
        clientes.altacliente(self.registrocli)
        self.listarclientes()
        self.limpiarcli()


    def listarclientes(self):
        listado = clientes.mostrarclientes()
        self.listclientes.clear()
        for registro in listado:
            self.listclientes.append(registro)

    def cargarcliente(self, widget):
        clientes.cargarcliente(self.listaclientes, self.liscmb, self.treeclientes, self.entclifac)

    def bajacliente(self, widget):
        dni = self.entdni.get_text()
        clientes.bajacliente(dni)
        self.listarclientes()
        self.limpiarcli()

    def modifcliente(self, widget):
        self.registrocli = []
        self.liscmb = []
        indexp = self.cmbprov.get_active()
        modelp = self.cmbprov.get_model()
        itemp = modelp[indexp][0]
        indexm = self.cmbmuni.get_active()
        modelm = self.cmbmuni.get_model()
        itemm = modelm[indexm][0]
        self.liscmb = [itemp, itemm]
        for i in range(4):
            self.registrocli.append(self.listaclientes[i].get_text())
        self.registrocli = self.registrocli + self.liscmb
        clientes.modifcliente(self.registrocli)
        self.listarclientes()
        self.limpiarcli()

    def limpiarcli(self):
        for registro in  self.listaclientes:
            registro.set_text("")

    """ alta camareros """

    def altacam(self, widget):
        datoscam = []
        for i in range(3):
            datoscam.append(self.listacam[i].get_text())

        camareros.altacama(datoscam)
        self.listarcamareros()
        self.limpiarcam()

    def limpiarcam(self):
        for registro in self.listacam:
            registro.set_text('')
        self.lblcodcam.set_text('')

    def listarcamareros(self):
        listado = camareros.mostrarcamareros()
        self.listcamareros.clear()
        for registro in listado:
            self.listcamareros.append(registro)

    def cargarcamarero(self, widget):
        listacam = [self.lblcodcam, self.entcam ]
        camareros.cargarcamarero(listacam, self.treecamareros, self.entcamfac)

    def bajacam(self, widget):
        id = self.lblcodcam.get_text()
        if id is not None:
            camareros.bajacam(id)
            self.listarcamareros()
            self.limpiarcam()
        else:
            print ('seleccion camarero')

    def modifcam(self, widget):
        lista = []
        lista.append(self.lblcodcam.get_text())
        for i in range(3):
            lista.append(self.listacam[i].get_text())
        camareros.modifcam(lista)
        self.limpiarcam()
        self.listarcamareros()

    """ gestion mesas """


    def limpiarmesa(self):
        self.entidmesa.set_text('')
        self.entmesa.set_text('')

    def altamesa(self, widget):
        idmesa = self.entidmesa.get_text()
        comensales = self.entmesa.get_text()
        mesas.altamesas(idmesa, comensales)
        self.limpiarmesa()
        self.listarmesas()

    def listarmesas(self):
        listado = mesas.listarmesas()
        self.listmesas.clear()
        for registro in listado:
            self.listmesas.append(registro)

    def cargarmesas(self, widget):
        mesas.cargarmesas(self.listamesa, self.treemesas)

    def modifmesa(self, widget):
        idmesa = self.entidmesa.get_text()
        comensales = self.entmesa.get_text()
        mesas.modifmesa(idmesa, comensales)
        self.limpiarmesa()
        self.listarmesas()

    def bajamesa(self, widget):
        idmesa = self.entidmesa.get_text()
        mesas.bajamesa(idmesa)
        self.limpiarmesa()
        self.listarmesas()

    """ gestion facturas """


#    def cargarfactura(self, widget):
#        listacam = [self.lblcodcam, self.entcam ]
#        reservas.cargarreserva(listacam, self.treecamareros, self.entcamfac)

    def limpiarfac(self):
        self.entserfac.set_text('')
        self.entcantidad.set_text('')
        for registro in self.listareserva:
            registro.set_text('')

    def mesa1(self, widget):

        libre = 0
        pagados = reservas.controlpagos(1)

        for registro in pagados:
            if str(registro) is 'NO':
                libre = 1
        listado = reservas.mostrarfacturas(1)
        self.listfact.clear()
        for registro in listado:
            self.listfact.append(registro)

        datos = []
        datos.clear()

        if self.reservas['mesa1'] == 0 and self.entclifac.get_text() != '' and self.entcamfac.get_text() != '' and libre == 0:
            datos.append(self.entclifac.get_text())
            datos.append(self.entcamfac.get_text())
            self.entmesafac.set_text('1')
            datos.append(self.entmesafac.get_text())
            self.entfechafac.set_text(self.hoy)
            datos.append(self.entfechafac.get_text())
            self.entpago.set_text('NO')
            datos.append(self.entpago.get_text())

            color = Gdk.color_parse('#FA8072')
            rgba = Gdk.RGBA.from_color(color)
            self.btnmesa1.override_background_color(0, rgba)
            self.reservas['mesa1'] = 1
            #for i in range(4):
            #    datos.append(self.listareserva[i].get_text())
            #datos.append('NO')
            print (datos)
            reservas.crearreserva(datos, 1)
            listado = reservas.mostrarfacturas(1)
            self.listfact.clear()
            for registro in listado:
                self.listfact.append(registro)
        self.limpiarfac()


    def mesa2(self, widget):

        libre = 0
        pagado2 = reservas.controlpagos(2)

        for registro in pagado2:
            if str(registro[0]) == 'NO' or registro == None:
                libre = 1

        listado = reservas.mostrarfacturas(2)
        self.listfact.clear()
        for registro in listado:
            self.listfact.append(registro)
        datos = []
        datos.clear()

        if self.reservas['mesa2'] == 0 and self.entclifac.get_text() != '' and self.entcamfac.get_text() != '' and libre == 0:
            self.entmesafac.set_text('2')
            self.entfechafac.s.gnome.orget_text(self.hoy)
            color = Gdk.color_parse('#FA8072')
            rgba = Gdk.RGBA.from_color(color)
            self.btnmesa2.override_background_color(0, rgba)
            self.reservas['mesa2'] = 1
            for i in range(4):
                datos.append(self.listareserva[i].get_text())
            datos.append('NO')
            reservas.crearreserva(datos, 2, self.listfact)
            listado = reservas.mostrarfacturas(2)
            self.listfact.clear()
            for registro in listado:
                self.listfact.append(registro)
        self.limpiarfac()

    def cargarreserva(self, widget):
        self.idfactura = reservas.cargarreserva(self.listareserva, self.treefacturas)
        self.listarcomandas(self.idfactura)


    """ gestion comandas """

    def altacomanda(self, widget):
        """ gestion comandas """
        comanda = []
        idfac = self.idfactura
        comanda.append(idfac)
        idser = self.entserfac.get_text()
        comanda.append(idser)
        plato = servicios.nombreplato(idser)
        comanda.append(plato)
        cantidad = self.entcantidad.get_text()
        comanda.append(cantidad)
        reservas.grabarcomanda(comanda)
        self.listarcomandas(idfac)

    def listarcomandas(self, idfactura):
        listado = reservas.listarcomandas(idfactura)
        self.listcomandas.clear()
        for registro in listado:
            self.listcomandas.append(registro)
        return listado

    def factura(self, widget):
        informes.factura(self.idfactura)
        self.mesaactiva = int(self.entmesafac.get_text())
        reservas.pagado(self.idfactura)
        color = Gdk.color_parse('white')
        rgba = Gdk.RGBA.from_color(color)
        self.mesas[self.mesaactiva-1].override_background_color(0, rgba)
        reservas.pagado(self.idfactura)

        self.limpiarfac()
        self.anulareserva()
        self.listarfacturas()

    def listarfacturas(self):
        var = int(self.mesaactiva)
        listado = reservas.mostrarfacturas(var)
        print (listado)
        self.listfact.clear()
        for registro in listado:
            self.listfact.append(registro)



    def anulareserva(self):
        if self.mesaactiva == 1:
            self.reservas['mesa1'] = '0'
        if self.mesaactiva == 2:
            self.reservas['mesa2'] = '0'
        if self.mesaactiva == 3:
            self.reservas['mesa3'] = '0'
        if self.mesaactiva == 4:
            self.reservas['mesa4'] = '0'
        if self.mesaactiva == 5:
            self.reservas['mesa5'] = '0'
        if self.mesaactiva == 6:
            self.reservas['mesa6'] = '0'
        if self.mesaactiva == 7:
            self.reservas['mesa7'] = '0'
        if self.mesaactiva == 8:
            self.reservas['mesa8'] = '0'


    """ funciones principales """

    def renovar(self, widget):
        self.limpiarcli()
        self.limpiarserv()
        self.limpiarcam()
        self.limpiarmesa()
        self.limpiarfac()

    def iniciarsala(self):
        i = 0

        for i in range(8):
            listado = reservas.controlpagos(i + 1)
            color = Gdk.color_parse('white')
            rgba = Gdk.RGBA.from_color(color)
            for registro in listado:
                if str(registro[0]) == 'NO':
                    color = Gdk.color_parse('#FA8072')
                    rgba = Gdk.RGBA.from_color(color)

            self.mesas[i].override_background_color(0, rgba)


    def salir(self, widget):
        bbdd.cerrarconexion()
        Gtk.main_quit()


""" lanzamos el programa """

if __name__ == '__main__':
    main = Restaurante()
    Gtk.main()
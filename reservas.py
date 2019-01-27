import bbdd

def crearreserva(datos, idmesa):
    try:
        bbdd.cur.execute('insert into facturas (dnicli, idcam, idmesa, fecha, pagado ) values (?,?,?,?,?)', datos)
        bbdd.conexion.commit()
        mostrarfacturas(idmesa)

    except Exception as err:
        print(err)
        bbdd.conexion.rollback()
        return True

def mostrarfacturas(idmesa):
    try:

        bbdd.cur.execute('select * from facturas where idmesa = ? ', (idmesa,))
        listado = bbdd.cur.fetchall()
        bbdd.conexion.commit()
        return listado
    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def cargarreserva(lista, treefactura):
    try:
        model, iter = treefactura.get_selection().get_selected()
        listres = []
        if iter != None:
            for j in range(6):
                listres.append(model.get_value(iter, j))

            for i in range(6):
                if i == 0:
                    var = str(listres[i])
                lista[i].set_text(str(listres[i]))

            return var
    except ValueError:
        print('error carga reservaaa')

def controlpagos(idmesa):
    try:
        bbdd.cur.execute('select pagado from facturas where idmesa = ? ', (idmesa,))
        valor = bbdd.cur.fetchall()
        bbdd.conexion.commit()
        return valor

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def grabarcomanda(lista):
    try:
        bbdd.cur.execute('insert into comandas (idfactura, idservicio, cantidad ) values (?,?,?)', (str(lista[0]), str(lista[1]), str(lista[3])),)
        bbdd.conexion.commit()


    except Exception as err:
        print(err)
        bbdd.conexion.rollback()
        return True

def listarcomandas(idfactura):
    try:
        bbdd.cur.execute('select idventa, c.idservicio, s.servicio, cantidad from comandas c, servicios s where c.idfactura = ? and s.Id = c.idservicio', (idfactura,))
        listado = bbdd.cur.fetchall()
        bbdd.conexion.commit()
        return listado

    except Exception as err:
        print(err)
        bbdd.conexion.rollback()
        return True

def pagado(factura):
    try:
        valor = 'SI'
        bbdd.cur.execute('update facturas set pagado = ? where id = ? ', (str(valor), str(factura)))
        bbdd.conexion.commit()

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()
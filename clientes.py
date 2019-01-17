import bbdd


""" manipulacion clientes """

def cargarprovi(listprov):
    try:
        listprov.clear()
        bbdd.cur.execute("select provincia from provincias")
        listado = bbdd.cur.fetchall()
        bbdd.conexion.commit()
        for row in listado:
            listprov.append(row)
    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def cargamuni(listmuni, cmbprov):
    try:
        index = cmbprov.get_active()
        model = cmbprov.get_model()
        item = model[index][0]
        listmuni.clear()
        bbdd.cur.execute("select id from provincias where provincia=?", (item,))
        id = bbdd.cur.fetchone()
        bbdd.cur.execute("select municipio from municipios where provincia_id=?", (id[0],))
        listado = bbdd.cur.fetchall()
        for row in listado:
            listmuni.append(row)

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def altacliente(registrocli):
    try:
        bbdd.cur.execute('insert into clientes (dni, apellido, nombre, direccion, provincia, municipio) values (?,?,?,?,?,?)', registrocli)
        bbdd.conexion.commit()

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()


def mostrarclientes():
    try:
        bbdd.cur.execute('select * from clientes order by apellido')
        listado = bbdd.cur.fetchall()
        bbdd.conexion.commit()
        return listado

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def cargarcliente(listaent, listacmb, treecliente, entclifac):
    try:
        model, iter = treecliente.get_selection().get_selected()
        lista = []
        for i in range(6):
            lista.append(model.get_value(iter, i))

        entclifac.set_text(str(lista[0]))
        for j in range(4):
            listaent[j].set_text(lista[j])
        bbdd.cur.execute("select id from provincias where provincia=?", (lista[4],))
        idp = bbdd.cur.fetchone()
        bbdd.cur.execute("select municipio from municipios where provincia_id=?", (idp[0],))
        listado = bbdd.cur.fetchall()
        i = 0
        listacmb[0].set_active(idp[0] - 1)
        for registro in listado:
            if registro[0] == lista[5]:
                listacmb[1].set_active(i)
            i += 1
        bbdd.conexion.commit()
    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def bajacliente(dni):
    try:
        if dni is not None:
            bbdd.cur.execute('delete from clientes where dni=?', (dni,))
            bbdd.conexion.commit()
        else:
            # ventana aviso
            print ('el cliente no existe')
    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()


def modifcliente(registrocli):
    try:
        if registrocli[0] is not None:
            bbdd.cur.execute('update clientes set apellido = ?, nombre = ?, direccion = ?, provincia = ?, municipio = ? where dni = ?', (str(registrocli[1]), str(registrocli[2]), str(registrocli[3]), str(registrocli[4]), str(registrocli[5]), str(registrocli[0],)))
            bbdd.conexion.commit()
        else:
            # ventana aviso
            print ('el cliente no existe')

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()



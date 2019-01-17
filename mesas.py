import bbdd


def altamesas(id, comensales):
    try:
        if comensales is not None:
            bbdd.cur.execute('insert into mesas (id, maxcomen) values (?,?)', (id, comensales),)
            bbdd.conexion.commit()

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def listarmesas():
    try:
        bbdd.cur.execute('select id, maxcomen from mesas')
        listado = bbdd.cur.fetchall()
        bbdd.conexion.commit()
        return listado

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def cargarmesas(lista, treemesas):
    try:
        model, iter = treemesas.get_selection().get_selected()
        listmes = []
        if iter != None:
            for i in range(2):
                listmes.append(model.get_value(iter, i))
            for j in range(2):
                lista[j].set_text(str(listmes[j]))
    except:
        print('error carga mesas')


def modifmesa(id, comen):
    try:
        bbdd.cur.execute('update mesas set maxcomen = ? where id = ?', (str(comen), str(id)))
        bbdd.conexion.commit()

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()


def bajamesa(id):
    try:
        if id is not None:
            bbdd.cur.execute('delete from mesas where id=?', (id,))
            bbdd.conexion.commit()
        else:
            # ventana aviso
            print ('la mesa no existe')
    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

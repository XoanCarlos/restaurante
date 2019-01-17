import bbdd
from Crypto.Cipher import DES

def altacama(listado):
    try:
        if listado[1] == listado[2]:
            des = DES.new('12345678', DES.MODE_ECB)
            passw = des.encrypt(listado[1])
            bbdd.conexion.text_factory = str
            bbdd.cur.execute('insert into camareros (nombre, passwd) values (?,?)', (listado[0], passw))
            bbdd.conexion.commit()

        else:
            print('contraseñas diferentes')

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def mostrarcamareros():
    try:
        bbdd.cur.execute('select idcam, nombre from camareros')
        listado = bbdd.cur.fetchall()
        bbdd.conexion.commit()
        return listado

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def cargarcamarero(lista, treecamareros, entcamfac):
    try:
        model, iter = treecamareros.get_selection().get_selected()
        listcam = []
        if iter != None:
            for i in range(2):
                listcam.append(model.get_value(iter, i))
            for j in range(2):
                lista[j].set_text(str(listcam[j]))
        entcamfac.set_text(str(listcam[0]))
    except:
        print('error carga camarero')

def bajacam(id):
    try:
        if id is not None:
            bbdd.cur.execute('delete from camareros where idcam=?', (id,))
            bbdd.conexion.commit()
        else:
            # ventana aviso
            print ('el camarero no existe')
    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()

def modifcam(lista):
    try:
        if lista[2] == lista[3]:
            des = DES.new('12345678', DES.MODE_ECB)
            passm = des.encrypt(lista[2])
            bbdd.conexion.text_factory = str
            bbdd.cur.execute('update camareros set nombre = ?, passwd = ? where idcam = ?', (str(lista[1]), str(passm), str(lista[0])))
            bbdd.conexion.commit()

    except bbdd.sqlite3.OperationalError as e:
        print(e)
        bbdd.conexion.rollback()


import sqlite3


try:
    """ datos conexion """

    bbdd = 'restaurante.sqlite'
    conexion = sqlite3.connect(bbdd)
    cur = conexion.cursor()
    print ('base de datos conectada')
except sqlite3.OperationalError as e:
    print (e)

def cerrarconexion():
    try:
        conexion.close()
        print ('base de datos cerrada')
    except sqlite3.OperationalError as e:
        print (e)



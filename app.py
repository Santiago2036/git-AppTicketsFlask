from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from config import config



app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='admin'
app.config['MYSQL_PASSWORD']='2036'
app.config['MYSQL_DB']='tickets'
conexion=MySQL(app)

@app.route('/')
def inicio():
    return render_template('creacionTicket.html')

@app.route("/recuperaRegistros")##ENLISTA TODOS LOS TICKETS
def listar_tiquetes():
        cur= conexion.connection.cursor()
        cur.execute('SELECT * FROM registrotiquetes ')
        conexion.connection.commit()

        datos=cur.fetchall()
        lista_Datos=list(datos)
        for i in lista_Datos:
            print("TICKET ENLISTADO")
            print(i ,end="\n")

        return "TICKETS ENLISTADOS!!"

@app.route("/consulta_ticket", methods=['POST'])##ENLISTA 1 TICKET ESPECIFICADO POR EL USUARIO
def consulta_tiquetes():
        if request.method == 'POST':
            IDENTIFICACION = request.form['ID']
            cur= conexion.connection.cursor()
            cur.execute("SELECT * FROM registrotiquetes WHERE ID = '{0}'".format(IDENTIFICACION) )
            conexion.connection.commit()
            datos=cur.fetchall()
            print(datos)
            return "CONSULTA EJECUTADA!!"

@app.route("/edita_ticket",methods=['POST'])##EDITA UN TICKETS
def edita_tiquete():
        if request.method == 'POST':

            IDENTIFICACION = request.form['ID']
            USUARIOS = request.form['USUARIO']
            FechaCreacion = request.form['fechaCreacion']
            FechaActualizacion = request.form['fechaActualizacion']
            Estatus = request.form['estatus']

            print(IDENTIFICACION)
            cur= conexion.connection.cursor()
            cur.execute("UPDATE registrotiquetes SET USUARIO='{0}' WHERE ID ='{1}'".format(USUARIOS,IDENTIFICACION))
            conexion.connection.commit()

            datos=cur.fetchall()
            print(datos)
            return "TICKET EDITADO CORRECTAMENTE!!"

@app.route("/elimina_ticket", methods=['POST'])##ELIMINA UN TICKET
def elimina_tiquete():
        if request.method == 'POST':
            IDENTIFICACION = request.form['ID']
            print(IDENTIFICACION)
            cur= conexion.connection.cursor()
            cur.execute("DELETE FROM registrotiquetes WHERE ID = '{0}'".format(IDENTIFICACION))
            conexion.connection.commit()
            datos=cur.fetchall()
            print(datos)
            return "TICKET ELIMINADO!"


@app.route("/crear_ticket",methods=['POST'])##CREA UN TICKET
def crear_tiquete():
        if request.method == 'POST':
            ID = request.form['ID']
            USUARIO = request.form['USUARIO']
            fechaCreacion = request.form['fechaCreacion']
            fechaActualizacion = request.form['fechaActualizacion']
            estatus = request.form['estatus']

            print (ID)
            print (USUARIO)
            print (fechaCreacion)
            print (fechaActualizacion)
            print (estatus)

            cur= conexion.connection.cursor()
            cur.execute('INSERT INTO registrotiquetes (ID,USUARIO,fechaCreacion,fechaActualizacion,estatus)VALUES(%s,%s,%s,%s,%s)',
                        (ID,USUARIO,fechaCreacion,fechaActualizacion,estatus))
            conexion.connection.commit()

            datos=cur.fetchall()
            print(datos)
            return "SE AGREGO TICKET CORRECTAMENTE!!"



if __name__== '__main__': ##llamado del programa app
    app.config.from_object(config['development'])
    app.run(debug=True, port=3306)##llamado del programa app con el respectivo puerto y el debug para que el servidor se reinicie automaticamente cuando ocurra una modificacion

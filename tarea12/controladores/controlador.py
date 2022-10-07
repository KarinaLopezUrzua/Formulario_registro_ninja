from tarea12 import app
from flask import render_template, redirect, session, request 
from tarea12.modelos.clases import Usuarios

#RUTAS FORMULARIO READ
@app.route("/") 
def formulario_raiz():
    return render_template("formulario.html") #Pagina inicio se dirige a html hijo

#RUTA CREAD
@app.route("/crear", methods=["POST"]) #ruta que se redigire action del formulario
def crear_usuario():
    datos = { #creamos un diccionario que obtendra la informacion de nuestro formulario
        "nombre":request.form["nombre"], #["nombre"] es el name que se coloco en el imput del formulario
        "ubicacion":request.form["ubicacion"],
        "lenguaje":request.form["lenguaje"],
        "comentario":request.form["comentario"],
    }
    if not Usuarios.validar_formulario(request.form):
        print(datos)
        # redirigir a la ruta donde se renderiza el formulario 
        return redirect('/')
    print(datos)
    id_usuario = Usuarios.registro_usuario(datos) #le agregamos una variable para poder retornar un numero y asi traquear al usuario para darle seguimiento con session. se llama al metodo para guardar la informacion en la base de datos
    print(id_usuario)
    session["id_usuario"] = id_usuario #estamos almacenando la variable en una clave
    return redirect(f"/usuario/{session['id_usuario']}") #se redirige a la pagina donde se muestra la informacion del usuario
#tenemos que concatenar, con formart y comillas simples


#ruta read para mostrar la informacion de un usuario
@app.route("/usuario/<int:id_usuario>")
def ver_usuario(id_usuario):
    datos = {
        "id_usuario": id_usuario
    }
    ver_un_usuario = Usuarios.obtener_un_usuario(datos)
    return render_template("info_un_usuario.html", ver_un_usuario=ver_un_usuario)

@app.errorhandler(404)
def pagina_no_encontrada():
    return  'ESTA RUTA NO FUE ENCONTRADA', 404  

""" colocar en TODAS las rutas GET
    if "id_usuario" not in session:
        return redirect("/")
"""



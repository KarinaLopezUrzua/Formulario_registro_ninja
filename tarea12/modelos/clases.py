from cgitb import strong
from tkinter.ttk import Style
from tarea12.config.mysqlconnection import conectarMySQL
from flask import flash

class Usuarios:
    def __init__(self, data): #en cada uno de los atributos de objetos estamos almacenando el valor de la clave de ese diccionario que obtenemos de la bd de nuestra tabla 
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.ubicacion = data["ubicacion"]
        self.lenguaje = data["lenguaje"]
        self.comentarios = data["comentarios"]
        self.created_at = data["created_at"]
        self.update_at = data["update_at"] #lo anote mal en la tabla que realice

    @classmethod # ahora usamos métodos de clase para consultar o leer nuestra base de datos. NADA MAS
    def obtener_todo(cls):
        query = "SELECT * FROM usuarios;" #aqui llamamos a la tabla e nuestra base de datos
        results = conectarMySQL('encuesta_dojo_schema').query_db(query) #result serian un diccionario en donde conectamos con el nombre de nuestra base de datos y  vamos a llamar a la función conectarMySQL con el esquema al que te diriges
        
        usuarios_dojo_instancias = []   # creamos una lista vacía para agregar nuestras instancias de usuarios
        for usuario_variable in results: # Iterar sobre los resultados de la base de datos y crear instancias de usuarios_instancias con cls
            usuarios_dojo_instancias.append(cls(usuario_variable)) #convertimos una lista de diccionarios en una lista de objetos
        return usuarios_dojo_instancias #retornamos una lista de objetos, lo transformamos a un objeto para poder usarlo en logica compleja desde html

#METODO CREATE con INSERT
    @classmethod
    def registro_usuario(cls, data): #(nombre de las columnas en nuestra tabla y en VALUES nombre de las claves de nuestro diccionario del controlador de forma sanitizada)
        query = """INSERT INTO usuarios (nombre, ubicacion, lenguaje, comentarios) 
        VALUES(%(nombre)s, %(ubicacion)s, %(lenguaje)s, %(comentario)s);""" #se coloca al final NOW(), NOW()), solo si por defecto nuesrta tabla no lo tiene predeterminado y arriba created_at y update_at
        return conectarMySQL('encuesta_dojo_schema').query_db(query, data)
#no es necesario transformsarlo en objeto ya que solo estamos guardando informacion

#para obtener un usuario a traves de su id
    @classmethod  # ahora usamos métodos de clase para consultar nuestra base de datos de forma sanitizada
    def obtener_un_usuario(cls, data):
        query = "SELECT * FROM usuarios WHERE id=%(id_usuario)s;" #aca la variable que queremos es el WHERE id=1 (2 o 3, etc), debemos sanitizarla con % y s
        results =  conectarMySQL('encuesta_dojo_schema').query_db(query, data)
        return cls(results[0]) #aca retorna solo el diccionario, no objetos

    @staticmethod
    def validar_formulario(usuario):
        validar = True # asumimos que esto es true
        if len(usuario['nombre']) < 5:
            flash("ATENCIÓN ¡NOMBRE COMPLETO debe tener al menos 5 caracteres!")
            validar = False
        if len(usuario['comentario']) < 3:
            flash("ATENCIÓN ¡COMENTARIOS debe tener al menos 3 caracteres!") #en el formulario sale que es opcion, pero lo puse para practicar
            validar = False
        if (usuario['ubicacion']) == "":
            flash("ATENCIÓN ¡Debe seleccionar una UBICACIÓN!") 
            validar = False
        if (usuario['lenguaje']) == "":
            flash("ATENCIÓN ¡Debe seleccionar una LENGUAJE!") 
            validar = False
        return validar

from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
#modelo de la clase dojo
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.ubicacion = data['ubicacion']
        self.idioma = data['idioma']
        self.comentario = data['comentario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#conseguir todos los Dojos
    @classmethod
    def get_last_dojo(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL('db_encuesta_dojo').query_db(query)
        return Dojo(results[0])

#guardar dojos
    @classmethod
    def save (cls, data):
        query = "INSERT INTO dojos (nombre, ubicacion, idioma, comentario) VALUES (%(nombre)s,%(ubicacion)s,%(idioma)s, %(comentario)s);"
        return connectToMySQL('db_encuesta_dojo').query_db(query, data)
        
    
    @staticmethod
    def is_valid(dojo):
        is_valid = True
        if len(dojo['nombre']) < 3:
            is_valid = False
            flash("Tu nombre debe tener almenos 3 caracteres")
        if len(dojo['ubicacion']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(dojo['idioma']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(dojo['comentario']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid
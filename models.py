from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from conexion.conexion import obtener_conexion

class Usuario(UserMixin):
    def __init__(self, id, usuario, password):
        self.id = id
        self.usuario = usuario
        self.password = password

    @classmethod
    def get_by_id(cls, user_id):
        conexion = obtener_conexion()
        if not conexion:
            return None
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id, usuario, password FROM usuarios WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        conexion.close()

        if user_data:
            return cls(id=user_data['id'], usuario=user_data['usuario'], password=user_data['password'])
        return None

    @classmethod
    def get_by_username(cls, username):
        conexion = obtener_conexion()
        if not conexion:
            return None
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id, usuario, password FROM usuarios WHERE usuario = %s", (username,))
        user_data = cursor.fetchone()
        cursor.close()
        conexion.close()

        if user_data:
            return cls(id=user_data['id'], usuario=user_data['usuario'], password=user_data['password'])
        return None

    @classmethod
    def crear(cls, username, password_plana):
        conexion = obtener_conexion()
        if not conexion:
            return False
        
        # Hash seguro de la contraseña
        password_hashed = generate_password_hash(password_plana)
        
        try:
            cursor = conexion.cursor()
            query = "INSERT INTO usuarios (usuario, password) VALUES (%s, %s)"
            cursor.execute(query, (username, password_hashed))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception:
            conexion.rollback()
            conexion.close()
            return False

    def check_password(self, password_plana):
        return check_password_hash(self.password, password_plana)
from .entities.usuario import Usuario
from .entities.tipo_de_usuario import TipoDeUsuario
from werkzeug.security import check_password_hash


class ModeloUsuario:
    @classmethod
    def login(self, db, usuario):
        cursor = db.connection.cursor()
        sql = f"SELECT id, nombre, password FROM usuario WHERE nombre = '{usuario.nombre}'"
        cursor.execute(sql)
        data = cursor.fetchone()
        coincide = check_password_hash(data[2], usuario.password)
        if coincide:
            return Usuario(data[0], data[1], None, None)
        else:
            return None

    @classmethod
    def obtener_por_id(self, db, id):
        cursor = db.connection.cursor()
        sql = f"SELECT USU.id, USU.nombre, TIP.id, TIP.nombre FROM usuario AS USU JOIN tipo_de_usuario AS TIP ON USU.tipoUsuarioId = TIP.id WHERE USU.id = {id}"
        cursor.execute(sql)
        data = cursor.fetchone()
        tipoUsuario = TipoDeUsuario(data[2], data[3])
        usuario_logeado = Usuario(data[0], data[1], None, tipoUsuario)
        return usuario_logeado

from flask_login import UserMixin


class Usuario(UserMixin):

    def __init__(self, id, nombre, password, tipoUsuario):
        self.id = id
        self.nombre = nombre
        self.password = password
        self.tipoUsuario = tipoUsuario

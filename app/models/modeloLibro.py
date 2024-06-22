from .entities.libro import Libro
from .entities.author import Author


class ModeloLibro():
    @classmethod
    def listar(self, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT LIB.isbn, LIB.titulo, AUT.nombre, AUT.fecha_de_nacimiento, LIB.ano_de_edicion FROM libro as LIB JOIN author as AUT WHERE LIB.author_id = AUT.id ORDER BY LIB.isbn'
            cursor.execute(sql)
            data = cursor.fetchall()
            libros = []
            for i in data:
                author = Author(None, i[2], i[3])
                libro = Libro(i[0], i[1], author, i[4])
                libros.append(libro)
            return libros
        except Exception as e:
            print(e)

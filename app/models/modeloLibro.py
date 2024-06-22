from .entities.libro import Libro
from .entities.author import Author


class ModeloLibro():
    @classmethod
    def listar(db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT LIB.isbn, LIB.titulo, LIB.autor_id, LIB.ano_edicion FROM libro as LIB JOIN author as AUT WHERE LIB.author_id = AUT.id ORDER BY isbn'
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(e)

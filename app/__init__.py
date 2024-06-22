from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL

from .models.modeloLibro import ModeloLibro

app = Flask(__name__)

csrf = CSRFProtect()

db = MySQL(app)


@app.route('/')
def index():
    libros = ModeloLibro.listar(db)
    print(libros)
    data = {
        'libros': libros
    }
    return render_template('index.html', data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        return redirect(url_for('index'))
    return render_template('auth/login.html')


def pagina_no_encontrada(error):
    return render_template('errors/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app

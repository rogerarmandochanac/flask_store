from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
from flask_login import LoginManager
from flask_login import login_user

from .models.modeloLibro import ModeloLibro
from .models.modeloUsuario import ModeloUsuario
from .models.entities.usuario import Usuario

app = Flask(__name__)

csrf = CSRFProtect()

login_manager_app = LoginManager(app)

db = MySQL(app)


@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.obtener_por_id(db, id)


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
        usuario = Usuario(None, request.form['usuario'],
                          request.form['contraseña'], None)
        usuarioLogeado = ModeloUsuario.login(db, usuario)
        if usuarioLogeado:
            login_user(usuarioLogeado)
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    return render_template('auth/login.html')


@app.route('/password/<data>')
def generate_password(data):
    info = generate_password_hash(data, method='pbkdf2:sha256')
    return f'encriptado:{info} largo {len(info)}'


def pagina_no_encontrada(error):
    return render_template('errors/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app

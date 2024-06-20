from app import inicializar_app
from config import config

development = config['development']

app = inicializar_app(development)


if __name__ == '__main__':
    app.run()

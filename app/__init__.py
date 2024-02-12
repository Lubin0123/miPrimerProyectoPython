# Importar la clase Flask y SQLAlchemy desde sus respectivos modelos
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

# Crear una instancia de LoginManager para manejar la autenticación del usuario
login_manager = LoginManager()
db = SQLAlchemy()
# Definir la función 'create_app' para configurar y crear la aplicación Flask
def create_app():
    # Crear una instancia de la aplicación Flask
    app = Flask(__name__)

    # Configurar la aplicación utilizando una clase de configuración en 'config.Config'
    app.config.from_object('config.Config')
    
    # Configurar una clave secreta para la aplicación (importante para la seguridad)
    app.config['SECRET_KEY'] = os.urandom(24)
    bcrypt = Bcrypt(app)
    # Inicializar la instancia de SQLAlchemy ('db') con la aplicación Flask
    db.init_app(app)

    # Inicializar la instancia de LoginManager ('login_manager') con la aplicación Flask
    login_manager.init_app(app)
    login_manager.login_view = 'autentificacion.login'

    # Definir una función para cargar usuarios durante la autenticación
    @login_manager.user_loader
    def load_user(user_id):
       
        # en este lugar realizo la importacion porque al hacerlo arriba aun no existe el obejto db y no puede inicializar porque aun no existe, asi que entonces lo importo aca abajo para que se ejecute en el mometo en que ya este creado 
        from app.models.Clientes import Clientes
         # Utilizar el ID del usuario para buscar y cargar el usuario desde la base de datos
        return Clientes.query.get(int(user_id))
    
    # Importar las rutas desde los módelos y registrarlas en la aplicación
    from app.routes import clienteRoute, productoRoute, autentificacionRoute, facturaVentasRoute
    app.register_blueprint(clienteRoute.bp)
    app.register_blueprint(productoRoute.bp)
    app.register_blueprint(autentificacionRoute.bp)
    app.register_blueprint(facturaVentasRoute.bp)

    # Retornar la aplicación configurada
    return app

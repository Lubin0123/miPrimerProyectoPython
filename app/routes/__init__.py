from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import clienteRoute, productoRoute,autentificacionRoute, facturaVentasRoute,carritoVentasRoute,administradorRoute
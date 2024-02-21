from flask_login import UserMixin
from app import db

class Clientes(db.Model, UserMixin):
    __tablename__ = "cliente"
    idClientes = db.Column(db.Integer, primary_key=True)
    nombreClientes = db.Column(db.String(255), nullable=False)
    cedulaClientes = db.Column(db.String(255), nullable=False)
    correoClientes = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    facturas = db.relationship('FacturaVentas')
    rol = db.Column(db.String(20), default='usuario')


    def get_id(self):
        return str(self.idClientes)
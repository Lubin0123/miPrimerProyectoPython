from flask_login import UserMixin
from app import db

class Clientes(db.Model, UserMixin):
    __tablename__ = "cliente"
    idClientes = db.Column(db.Integer, primary_key=True)
    nombreClientes = db.Column(db.String(255), nullable=False)
    cedulaClientes = db.Column(db.String(255), nullable=False)
    correoClientes = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    facturaVentas = db.relationship('FacturaVentas', backref='miCliente', lazy=True,overlaps="facturaVentas")

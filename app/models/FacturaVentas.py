from app import db
from app.models.Clientes import Clientes
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class FacturaVentas(db.Model):
    __tablename__ = "facturaVenta"
    idFacturaVenta = db.Column(db.Integer, primary_key=True)
    idClientes = db.Column(db.Integer, db.ForeignKey('Clientes.idClientes'), nullable=False)
    horaFacturaVenta = db.Column(db.Time, nullable=False)
    totalFacturaVenta = db.Column(db.String(255), nullable=False)
    clienteRelacion = db.relationship('Clientes', backref='facturaVentas', lazy=True)

from flask_login import UserMixin
from app import db
from datetime import datetime

class FacturaVentas(db.Model, UserMixin):
    __tablename__ = "facturaVenta"
    idFacturaVenta = db.Column(db.Integer, primary_key=True)
    idClientes = db.Column(db.Integer, db.ForeignKey('cliente.idClientes'), nullable=False)
    horaFacturaVenta = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    totalFacturaVenta = db.Column(db.Integer, nullable=False)
    cliente = db.relationship('Clientes', backref='facturasVentas', lazy=True, overlaps="miCliente")

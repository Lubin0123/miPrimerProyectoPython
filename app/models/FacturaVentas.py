from flask_login import UserMixin
from app import db
from app.models.Clientes import Clientes
from app.models.Productos import Productos
from datetime import datetime

class FacturaVentas(db.Model, UserMixin):
    __tablename__ = "facturaVenta"
    idFacturaVentas = db.Column(db.Integer, primary_key=True)
    idClientes = db.Column(db.Integer, db.ForeignKey('cliente.idClientes'), nullable=False)
    horaFacturaVentas = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    totalFacturaVentas = db.Column(db.Integer, nullable=False)
    producto = db.relationship("Productos", secondary="detalleVenta",back_populates="factura")
    

  
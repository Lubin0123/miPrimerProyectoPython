from app import db


class CarritoVentas (db.Model):
    __tablename__ = "carritoventas"
    idProductos = db.Column(db.Integer, primary_key=True)
    descripcionProductos= db.Column(db.String(255), nullable=False)
    precioProductos = db.Column(db.String(255),nullable=False)
    cantidadProductos = db.Column(db.String(255), nullable=False)

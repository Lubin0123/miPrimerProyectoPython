from app import db


class Producto(db.Model):
    idProductos = db.Column(db.Integer, primary_key=True)
    descripcionProductos= db.Column(db.String(255), nullable=False)
    precioProductos = db.Column(db.Integer,nullable=False)
    cantidadProductos = db.Column(db.Integer, nullable=False)
   

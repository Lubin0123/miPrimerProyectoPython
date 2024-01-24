from app import db


class productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProducto = db.Column(db.Integer, nullable=False)
    nombreproducto = db.Column(db.String(255), nullable=False)
   

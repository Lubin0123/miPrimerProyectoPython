from app import db


class Cliente(db.Model):
    idClientes = db.Column(db.Integer, primary_key=True)
    nombreClientes = db.Column(db.String(255), nullable=False)
    cedulaClientes = db.Column(db.Integer, nullable=False)
    correoClientes =db.colum(db.string(255), nullable=False)

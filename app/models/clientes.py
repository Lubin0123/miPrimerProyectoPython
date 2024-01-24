from app import db


class clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    documento = db.Column(db.Integer, nullable=False)
   

from backend import db
from datetime import datetime

class Device(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(100))
	valor = db.Column(db.Integer)
	hora = db.Column(db.DateTime)

	def __init__(self, nome, valor, hora):
                self.nome = nome
                self.valor = valor
                self.hora = hora

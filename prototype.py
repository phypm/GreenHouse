from backend import db
from datetime import datetime

class Device(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	posicaox = db.Column(db.Float)
	posicaoy = db.Column(db.Float)
	sensores = db.relationship('Measurement')
	
class Measurement(db.Model):
        id_device = db.Column(db.Integer, db.ForeignKey('device.id'))
        temp = db.Column(db.Float)
        lum = db.Column(db.Float)
        time = db.Column(db.DateTime, primary_key= True)

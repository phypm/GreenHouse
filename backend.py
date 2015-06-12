from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
import json

prog = Flask(__name__)
prog.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///greenhouse'
db = SQLAlchemy(prog)

from  prototype import *


@prog.route ('/ghtest')
def index():
    return "Greenhouse, as rotas utilizadas foram: '/post/greenhouse' e '/get/greenhouse'"

@prog.route('/greenhouse', methods=['GET'])
def device():
	sensores = []
	for i in Device.query.all():
		print i.time, i.temp, i.lum
		sensores.append({'Horario de Medicao': i.date.isoformat(), 'Temperatura': i.temp, 'Luminosidade': i.lum})

	return json.dumps(sensores)


@prog.route('/measurement', methods=['POST'])
def exibir_dados():
	if not request.json:
		return jsonify({'status': False})

	p = request.get_json()
	s = Measurement()
	s.id_device = p['id']
	s.temp = p['Temperatura']
	s.lum = p['Luminosidade']
	s.time = datetime.today()
	db.session.add(s)
	db.session.commit()

	return jsonify({'status:': True})

@prog.route('/greenhouse/new', methods=['POST'])
def exibir_dados2():
	if not request.json:
		return jsonify({'status': False})

	p = request.get_json()
	m = Device()
	m.posicaox= p['Posicao em X']
	m.posicaoy= p ['Posicao em Y']
	db.session.add(m)
	db.session.commit()

	return jsonify({'status:': True})    

if (__name__)== '__main__':
    prog.run(debug = True)

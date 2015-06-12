from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json

prog = Flask(__name__)
prog.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:////greenhouse'
db = SQLAlchemy(prog)

from  prototype import *


@prog.route ('/ghtest')
def index():
    return "Greenhouse, as rotas utilizadas foram: '/post/greenhouse' e '/get/greenhouse'"

@prog.route('/greenhouse', methods=['GET'])
def device():
	sensores = []
	for i in Device.query.all():
		print i.nome, i.valor, i.hora
		sensores.append({'id': i.id, 'nome': i.nome, 'valor': i.valor, 'hora': i.hora})

	return json.dumps(sensores)


@prog.route('/measurement', methods=['POST'])
def exibir_dados():
	if not request.json:
		return jsonify({'status': False})

	p = request.get_json()
	s = Device()
	s.temp = p['Temperatura']
	s.lum = p['Luminosidade']
	s.time = p ['Horario da medicao']
	db.session.add(s)
	db.session.commit()

	return jsonify({'status:': True})

@prog.route('/post/greenhouse', methods=['POST'])
def exibir_dados():
	if not request.json:
		return jsonify({'status': False})

	p = request.get_json()
	m = Measurement()
	m.id= m('ID')
	m.posicaox= m('Posicao em X')
	m.posicaoy= m ('Posicao em y')
	db.session.add(s)
	db.session.commit()

	return jsonify({'status:': True})    

if (__name__)== '__main__':
    prog.run(debug = True)

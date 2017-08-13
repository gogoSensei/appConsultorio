# -*- coding: utf-8 -*-
from flask import *
from Aplication.settings.db import conectionDb as db
from Aplication.settings import forms
import hashlib
import datetime
import sys,os
from flask_wtf import CSRFProtect

db = db()
app = Flask(__name__)
app.secret_key = 'angelesyoshua'
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def ini():
	#r = db.rawQuery('SELECT * FROM usuarios')
	#print(r)
	oment_form = forms.iniForm(request.form)
	return render_template('login.html', form = oment_form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	_form = forms.iniForm(request.form)
	if (request.method in ['POST'] and _form.validate()):
		_login = db.rawQuery("SELECT gr_login_user('{0}', '{1}')".format(_form.email.data, _form.password.data))[0][0]
		if (_login):
			return render_template('index.html', form = _form)
		flash('El usuario o contraseña es incorrecta')
	return render_template('login.html', form = _form)

@app.route("/pacientes", methods=['GET', 'POST'])
def pacientes():
	print('yes pass for here')
	return render_template('pacientes.html')




"""
Modo de agregar password con cifrado
import hashlib
pass = b"kmotin818"
hashlib.sha224(pass).hexdigest()
"""
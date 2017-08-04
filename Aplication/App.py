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
		r = db.rawQuery("SELECT * FROM usuarios WHERE email = TRIM('{0}')".format(_form.email.data))
		print(r)
		if (r == []):
			flash('El usuario no existe')
			return render_template('login.html', form = _form)
		for _data in r:
			password = _data[3]
			_compare = (_form.password.data).encode()
			if (password != hashlib.sha224(_compare).hexdigest()):
				flash('La contraseña es incorrecta')
				return render_template('login.html', form = _form)
		return render_template('index.html', form = _form)
	#r_make = make_response()
	return render_template('login.html', form = _form)

"""
Modo de agregar password con cifrado
import hashlib
pass = b"kmotin818"
hashlib.sha224(pass).hexdigest()
"""
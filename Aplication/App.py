# -*- coding: utf-8 -*-
from flask import *
from Aplication.settings.db import conectionDb as db
from Aplication.settings import forms
from flask_wtf import CSRFProtect
from Aplication.settings.config import ConfigDevelop
from datetime import datetime, timedelta
import hashlib
import sys,os

db = db()
app = Flask(__name__)
app.config.from_object(ConfigDevelop)
csrf = CSRFProtect()

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
      session['usermail'] = _form.email.data
      return redirect(url_for('index'))
    flash('El usuario o contraseña es incorrecta')
  return render_template('login.html', form = _form)

@app.route("/index", methods=['GET', 'POST'])
def index():
  _form = forms.iniForm(request.form)
  return render_template('index.html')

@app.route("/pacientes", methods=['GET', 'POST'])
def pacientes():
  print('yes pass for here')
  return render_template('pacientes.html')

@app.before_request
def beforeRequest():
  try:
    if (datetime.now() >= session['lastUse']):
      session.pop('lastUse')
      session.pop('usermail')
      return redirect(url_for('ini'))
  except:
    session['lastUse'] = g.lastUse = datetime.now() + timedelta(minutes=5)
  print(str(session['lastUse']))

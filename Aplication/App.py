from flask import Flask,render_template, request, make_response
from Aplication.settings.db import conectionDb as db

app = Flask(__name__)
db = db()

@app.route('/')
def ini():
	r = db.rawQuery('SELECT * FROM usuarios')
	print(r)
	return render_template('login.html')

#@app.route("/login", methods=['GET', 'POST'])
#def login():

"""
Modo de agregar password con cifrado
import hashlib
pass = b"kmotin818"
hashlib.sha224(pass).hexdigest()
"""
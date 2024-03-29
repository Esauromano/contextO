from flask import Flask, request, flash, url_for, redirect, render_template
from flask_api import status
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:xmatrixy@127.0.0.1/contextO'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension
import json


class users(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   nombre = db.Column(db.String(50))
   data = db.Column(db.JSON())

def __init__(self, nombre, data):
   self.nombre = name
   self.data = data

def to_pretty_json(value):
    return json.dumps(value, sort_keys=True,
                      indent=4, separators=(',', ': '))

app.jinja_env.filters['tojson_pretty'] = to_pretty_json

@app.route('/')
def show_all():
	lusers = users.query.all()  #returns a Query object. 
	for user in lusers:
		print (user.nombre)

	#print (users.query.all())
	#return users.query.all().filter_by(id)
	return render_template('show_all.html', users = lusers)
	print(userByID)

@app.route('/user/<iden>')
def show_user(iden):
	userByID = users.query.filter_by(id=iden).first()
	print(userByID)
	#lusers = users.query.all()  #returns a Query object. 
	return render_template('show_one.html', users = userByID)

@app.route('/json/<iden>')
def show_json(iden):
	userByID = users.query.filter_by(id=iden).first_or_404(description='No hay dato alguno con ID = {}'.format(iden))
	yeisonStr = '{"codigo": 200, "mensaje":"Petición completada"}'
	yeison = json.loads(yeisonStr)
	if hasattr(userByID, 'data'):
		yeison['payload']=userByID.data
		print(userByID.data)
		return render_template('show_json.html', data = json.dumps(yeison))
	
from flask import Flask
from flask import make_response


app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>teste</h1>'
	

@app.route('/user/<name>')
def user(name):
	return '<h1>Olá {}, bem vindo!'.format(name)


@app.route('/teste')
def teste():
	response = make_response('<h1>Este doc carrega um cookie </h1>')
	response.set_cookie('answer', '42')
	return response



app.run(debug=True)

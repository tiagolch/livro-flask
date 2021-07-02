from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>teste</h1>'

@app.route('/user/<name>')
def user(name):
	return '<h1>Olá {}, bem vindo!'.format(name)